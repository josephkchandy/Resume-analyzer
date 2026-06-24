import os
import shutil
import tempfile
import uuid
from pathlib import Path
from threading import Lock

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from llama_index.core import Settings, VectorStoreIndex
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.llms.gemini import Gemini
from llama_index.readers.file import PDFReader
from werkzeug.utils import secure_filename

load_dotenv(override=True)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

# In-memory storage is suitable for a local/demo app. Use Redis or a database
# when deploying with multiple workers or when indexes must survive restarts.
INDEXES = {}
INDEX_LOCK = Lock()


def configure_models() -> None:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured. Add it to a .env file.")

    chat_model = os.getenv("GEMINI_CHAT_MODEL", "models/gemini-2.5-flash")
    if chat_model == "models/gemini-1.5-flash":
        chat_model = "models/gemini-2.5-flash"

    Settings.llm = Gemini(
        model=chat_model,
        api_key=api_key,
        temperature=0,
    )
    Settings.embed_model = GeminiEmbedding(
        model_name=os.getenv("GEMINI_EMBEDDING_MODEL", "models/gemini-embedding-001"),
        api_key=api_key,
    )


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/api/upload")
def upload_resume():
    uploaded_file = request.files.get("file")
    if uploaded_file is None or not uploaded_file.filename:
        return jsonify(error="No PDF was provided."), 400

    filename = secure_filename(uploaded_file.filename)
    if not filename.lower().endswith(".pdf"):
        return jsonify(error="Only PDF files are accepted."), 400

    temp_dir = Path(tempfile.mkdtemp(prefix="resumeai_"))
    pdf_path = temp_dir / filename

    try:
        configure_models()
        uploaded_file.save(pdf_path)

        documents = PDFReader().load_data(file=pdf_path)
        readable_documents = [doc for doc in documents if (doc.text or "").strip()]
        if not readable_documents:
            return jsonify(
                error="No readable text was found. The PDF may be scanned and require OCR."
            ), 422

        index = VectorStoreIndex.from_documents(readable_documents)
        query_engine = index.as_query_engine(similarity_top_k=5, response_mode="compact")
        summary_prompt = (
            "Analyze this resume and provide a concise professional summary with these "
            "sections: Profile, Key Skills, Experience Highlights, Education/Certifications, "
            "and 3 Practical Improvement Suggestions. Use only information in the document. "
            "Clearly state when a section is not present."
        )
        summary = str(query_engine.query(summary_prompt))

        document_id = uuid.uuid4().hex
        with INDEX_LOCK:
            INDEXES[document_id] = query_engine

        return jsonify(
            document_id=document_id,
            filename=filename,
            summary=summary,
        )
    except RuntimeError as exc:
        return jsonify(error=str(exc)), 500
    except Exception as exc:
        app.logger.exception("Resume processing failed")
        return jsonify(error=f"The PDF could not be processed: {exc}"), 500
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


@app.post("/api/ask")
def ask_resume():
    payload = request.get_json(silent=True) or {}
    document_id = str(payload.get("document_id", "")).strip()
    question = str(payload.get("question", "")).strip()

    if not document_id or not question:
        return jsonify(error="Both document_id and question are required."), 400
    if len(question) > 1000:
        return jsonify(error="Question is too long."), 400

    with INDEX_LOCK:
        query_engine = INDEXES.get(document_id)
    if query_engine is None:
        return jsonify(error="This resume session expired. Please upload the PDF again."), 404

    try:
        answer = str(
            query_engine.query(
                "Answer using only the uploaded resume. If the answer is not in the resume, "
                f"say that clearly. Question: {question}"
            )
        )
        return jsonify(answer=answer)
    except Exception as exc:
        app.logger.exception("Resume question failed")
        return jsonify(error=f"The question could not be answered: {exc}"), 500


@app.errorhandler(413)
def file_too_large(_error):
    return jsonify(error="The PDF exceeds the 10 MB limit."), 413


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
