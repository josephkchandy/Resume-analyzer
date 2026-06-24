# ResumeAI - UI + LlamaIndex integration

This project connects the supplied ResumeAI interface to a Flask backend. A user can upload a PDF resume, receive an AI-generated summary, and ask follow-up questions about that resume.
<img width="1897" height="911" alt="Screenshot 2026-06-24 102111" src="https://github.com/user-attachments/assets/601ae90c-1acd-4e29-a777-38886adf45fe" />


## Run locally

1. Create and activate a virtual environment:

   Windows:
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and add your Gemini API key:

   ```env
   GEMINI_API_KEY=your-gemini-api-key-here
   ```

4. Start the app:

   ```bash
   python app.py
   ```

5. Open `http://127.0.0.1:5000`.

## Structure

- `app.py` - Flask backend and LlamaIndex processing
- `templates/index.html` - integrated ResumeAI frontend
- `.env.example` - environment variables template
- `requirements.txt` - Python packages

## Important notes

- Never put the Gemini API key in frontend JavaScript.
- Uploaded PDFs are temporarily saved and deleted after indexing.
- Indexes are kept in server memory and disappear when the server restarts.
- Scanned/image-only PDFs require an OCR step, which is not included here.
- For production, add authentication, persistent/managed vector storage, rate limiting, malware scanning, and a background job queue for large files.
