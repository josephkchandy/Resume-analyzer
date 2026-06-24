---
name: Luminous Professional
colors:
  surface: '#fcf8fb'
  surface-dim: '#dcd9dc'
  surface-bright: '#fcf8fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f5'
  surface-container: '#f0edef'
  surface-container-high: '#eae7ea'
  surface-container-highest: '#e4e2e4'
  on-surface: '#1b1b1d'
  on-surface-variant: '#414755'
  inverse-surface: '#303032'
  inverse-on-surface: '#f3f0f2'
  outline: '#717786'
  outline-variant: '#c1c6d7'
  surface-tint: '#005bc1'
  primary: '#0058bc'
  on-primary: '#ffffff'
  primary-container: '#0070eb'
  on-primary-container: '#fefcff'
  inverse-primary: '#adc6ff'
  secondary: '#5d5e63'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfe4'
  on-secondary-container: '#626267'
  tertiary: '#5a5c60'
  on-tertiary: '#ffffff'
  tertiary-container: '#737479'
  on-tertiary-container: '#fdfcff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a41'
  on-primary-fixed-variant: '#004493'
  secondary-fixed: '#e3e2e7'
  secondary-fixed-dim: '#c6c6cb'
  on-secondary-fixed: '#1a1b1f'
  on-secondary-fixed-variant: '#46464b'
  tertiary-fixed: '#e2e2e7'
  tertiary-fixed-dim: '#c6c6cb'
  on-tertiary-fixed: '#1a1c1f'
  on-tertiary-fixed-variant: '#45474b'
  background: '#fcf8fb'
  on-background: '#1b1b1d'
  surface-variant: '#e4e2e4'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Inter
    fontSize: 34px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 17px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: -0.01em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.06em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 40px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The design system is rooted in **Modern Minimalism** with a heavy influence from **Glassmorphism**. It is designed to feel like a high-end productivity tool that is both intelligent and unobtrusive. The target audience is professionals who value clarity, precision, and a premium aesthetic.

The UI should evoke a sense of calm, confidence, and "digital air." By utilizing vast amounts of white space and translucent layering, the interface recedes to let the user's content—their career history—become the focal point. Interactions should feel fluid and lightweight, mimicking the tactile yet ethereal nature of frosted glass.

## Colors

The palette is strictly curated to maintain a "San Francisco" professional aesthetic. 

- **Primary Blue:** Used exclusively for high-intent actions, links, and active states. It should be vibrant but balanced against the neutrals.
- **Grays:** A tiered scale of soft grays is used for secondary text, borders, and subtle backgrounds to create depth without adding visual noise.
- **Translucency:** Backgrounds for floating elements (modals, sidebars, navigation) should use the `surface_glass` token with a `saturate(180%) blur(20px)` backdrop filter to maintain the glassmorphic theme.

## Typography

The design system uses **Inter** to achieve a functional, systematic, and clean look that mirrors SF Pro. 

- **Hierarchy:** Use bold weights for headlines to provide a clear anchor point for the eye. 
- **Tracking:** Generous tracking is applied to `label-caps` for an editorial feel. Negative letter spacing is applied to larger display type to maintain a tight, professional lockup.
- **Readability:** Body text is set at 17px to ensure maximum legibility for long-form resume content, following accessibility standards for high-density information.

## Layout & Spacing

This design system employs a **Fluid Grid** with fixed maximum constraints. 

- **Desktop:** 12-column grid with a 1200px max-width container. Content should be centered with 40px outer margins.
- **Mobile:** Single column with 20px side margins. 
- **Spacing Philosophy:** Use an 8px base unit. Elements are spaced generously; when in doubt, increase padding. Horizontal sections should be separated by `stack-lg` to prevent the UI from feeling "cramped" or "data-heavy."

## Elevation & Depth

Depth is created through **Glassmorphism** and **Ambient Shadows** rather than solid fills.

- **Level 1 (Base):** Pure white background.
- **Level 2 (Cards):** Subtle white fill with a 1px border (`rgba(0,0,0,0.05)`) and a soft, highly diffused shadow: `0 4px 24px rgba(0,0,0,0.04)`.
- **Level 3 (Overlays):** Glassmorphic surfaces with `backdrop-filter: blur(20px)`. These should have a slightly stronger shadow: `0 12px 40px rgba(0,0,0,0.08)`.

Avoid harsh black shadows or heavy inner glows. The goal is to simulate a soft light source directly above the screen.

## Shapes

The shape language is defined by extreme **Roundedness**. 

- **Standard Elements:** Use a 16px to 24px radius (Token: `rounded-xl` or higher).
- **Cards & Modals:** Always use at least 24px corner radii.
- **Buttons:** Fully pill-shaped (500px radius) to emphasize a friendly, touch-ready appearance. 

Maintain "nested corner" harmony: if a button is inside a card, the card's radius should be larger than the button's radius to ensure a balanced visual flow.

## Components

### Buttons
- **Primary:** Pill-shaped, Primary Blue background, white text. No shadow, or a very faint blue-tinted glow on hover.
- **Secondary:** Pill-shaped, light gray background (`#F2F2F7`), dark text.

### Input Fields
- **Style:** Minimalist. Use a subtle light gray background with no border in its default state. On focus, transition to a white background with a 2px Primary Blue border.
- **Radius:** 12px for standard fields.

### Cards
- **Elegant Container:** Used for resume sections (Experience, Education). White background, 24px radius, and the "Level 2" ambient shadow. Padding should be a minimum of 32px.

### Chips/Badges
- **Style:** Small, pill-shaped elements for "Skills" or "Status." Use high-transparency primary colors (e.g., `rgba(0,122,255,0.1)`) with matching text color.

### AI Assistant Bubble
- **Glassmorphic:** The chat or suggestion bubble should use the glass effect with a distinct 1px white inner-border to simulate the edge of a glass pane.