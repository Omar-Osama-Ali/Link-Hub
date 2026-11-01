# Let's write the redesigned production files with top-tier UI/UX refinements:
# - Premium typography (Inter / System font stack with enhanced tracking & weights)
# - Subdued elegant surface tokens matching the brand color palette (#000000, #080808, #101010, #151515, #D6B46A)
# - Refined button proportions (18px border radius, tactile active states, smooth hover transitions, subtle specular rim highlight)
# - Perfect accessibility & touch targets (min 56px height, WCAG AA contrast)
# - Zero fluff, zero footers, exact 6 links preserved in order (Portfolio, WhatsApp, Email, Phone Number, Telda, InstaPay)

improved_index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <title>Omar Osama | Official Links</title>
  <meta name="description" content="Official personal link hub for Omar Osama. Access portfolio, contact via WhatsApp, email, or phone, and access payment links.">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#000000">

  <!-- Canonical URL -->
  <link rel="canonical" href="https://omar-osama-ali.github.io/">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="Omar Osama | Official Links">
  <meta property="og:description" content="Official personal link hub for Omar Osama.">
  <meta property="og:url" content="https://omar-osama-ali.github.io/">

  <!-- Stylesheet -->
  <link rel="stylesheet" href="style.css">

  <!-- INSERT OFFICIAL GOOGLE SEARCH CONSOLE VERIFICATION META TAG HERE -->
</head>
<body>

  <main class="hub-container" role="main">
    <header class="profile-header">
      <h1 class="profile-name">Omar Osama</h1>
      <div class="gold-divider" aria-hidden="true"></div>
    </header>

    <nav class="links-nav" aria-label="Official Links">
      <!-- 1. Portfolio -->
      <a href="https://omar-osama-ali.github.io/" class="link-btn" target="_blank" rel="noopener noreferrer" data-link-name="portfolio">
        <span class="btn-icon" aria-hidden="true">
          <!-- Monitor / Laptop Icon -->
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/>
            <line x1="8" y1="21" x2="16" y2="21"/>
            <line x1="12" y1="17" x2="12" y2="21"/>
          </svg>
        </span>
        <span class="btn-label">Portfolio</span>
        <span class="btn-arrow" aria-hidden="true">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"/>
            <polyline points="12 5 19 12 12 19"/>
          </svg>
        </span>
      </a>

      <!-- 2. WhatsApp -->
      <a href="https://wa.me/201200140223" class="link-btn" target="_blank" rel="noopener noreferrer" data-link-name="whatsapp">
        <span class="btn-icon" aria-hidden="true">
          <!-- Message Circle Icon -->
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>
          </svg>
        </span>
        <span class="btn-label">WhatsApp</span>
        <span class="btn-arrow" aria-hidden="true">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"/>
            <polyline points="12 5 19 12 12 19"/>
          </svg>
        </span>
      </a>

      <!-- 3. Email -->
      <a href="mailto:omar.osama2011@yahoo.com" class="link-btn" data-link-name="email">
        <span class="btn-icon" aria-hidden="true">
          <!-- Envelope Icon -->
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
            <polyline points="22,6 12,13 2,6"/>
          </svg>
        </span>
        <span class="btn-label">Email</span>
        <span class="btn-arrow" aria-hidden="true">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"/>
            <polyline points="12 5 19 12 12 19"/>
          </svg>
        </span>
      </a>

      <!-- 4. Phone Number -->
      <a href="tel:+201200140223" class="link-btn" data-link-name="phone">
        <span class="btn-icon" aria-hidden="true">
          <!-- Telephone Handset Icon -->
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">
            <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
          </svg>
        </span>
        <span class="btn-label">Phone Number</span>
        <span class="btn-arrow" aria-hidden="true">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"/>
            <polyline points="12 5 19 12 12 19"/>
          </svg>
        </span>
      </a>

      <!-- 5. Telda -->
      <a href="https://telda.me/omarosama2011" class="link-btn" target="_blank" rel="noopener noreferrer" data-link-name="telda">
        <span class="btn-icon" aria-hidden="true">
          <!-- Minimal Card / Transfer Icon -->
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">
            <rect x="1" y="4" width="22" height="16" rx="2" ry="2"/>
            <line x1="1" y1="10" x2="23" y2="10"/>
          </svg>
        </span>
        <span class="btn-label">Telda</span>
        <span class="btn-arrow" aria-hidden="true">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"/>
            <polyline points="12 5 19 12 12 19"/>
          </svg>
        </span>
      </a>

      <!-- 6. InstaPay -->
      <a href="https://ipn.eg/S/omar.osama2011/instapay/8AsH4D" class="link-btn" target="_blank" rel="noopener noreferrer" data-link-name="instapay">
        <span class="btn-icon" aria-hidden="true">
          <!-- Fast Transfer / Payment Icon -->
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
          </svg>
        </span>
        <span class="btn-label">InstaPay</span>
        <span class="btn-arrow" aria-hidden="true">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"/>
            <polyline points="12 5 19 12 12 19"/>
          </svg>
        </span>
      </a>
    </nav>
  </main>

  <!-- Optional Analytics Script -->
  <script src="script.js"></script>
</body>
</html>
"""

improved_style_css = """/* ==========================================================================
   Omar Osama — Official Links | Redesigned Premium UI/UX
   ========================================================================== */

:root {
  --bg-primary: #000000;
  --bg-secondary: #080808;
  --surface-elevated: #101010;
  --surface-hover: #161616;
  
  --text-primary: #FFFFFF;
  --text-secondary: #B8B8B8;
  --text-muted: #858585;
  
  --accent-gold: #D6B46A;
  --gold-border: rgba(214, 180, 106, 0.22);
  --gold-glow: rgba(214, 180, 106, 0.08);
  
  --border-subtle: rgba(255, 255, 255, 0.09);
  --border-hover: rgba(255, 255, 255, 0.28);
  
  --radius-btn: 18px;
  --max-width: 500px;
  --transition-smooth: 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Reset & Base Setup */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  -webkit-text-size-adjust: 100%;
}

body {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background-color: var(--bg-primary);
  color: var(--text-primary);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow-x: hidden;
  position: relative;
}

/* Subtle ambient radial background glow behind profile */
body::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100%;
  max-width: 600px;
  height: 320px;
  background: radial-gradient(circle at 50% 0%, rgba(214, 180, 106, 0.04) 0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
}

/* Main Hub Container */
.hub-container {
  width: 100%;
  max-width: var(--max-width);
  margin-inline: auto;
  padding: clamp(32px, 6vh, 56px) clamp(20px, 5vw, 24px);
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  z-index: 1;
}

/* Profile Header */
.profile-header {
  text-align: center;
  margin-bottom: clamp(32px, 6vh, 44px);
  width: 100%;
}

.profile-name {
  font-size: clamp(2.1rem, 5.5vw, 2.6rem);
  font-weight: 300;
  letter-spacing: 0.06em;
  color: var(--text-primary);
  line-height: 1.15;
}

.gold-divider {
  width: 32px;
  height: 2px;
  background-color: var(--accent-gold);
  margin: 18px auto 0;
  border-radius: 2px;
  box-shadow: 0 0 12px var(--gold-glow);
}

/* Links Navigation */
.links-nav {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: clamp(12px, 2vh, 16px);
}

/* Link Button Component */
.link-btn {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  min-height: 64px;
  padding: 16px 22px;
  background-color: var(--surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-btn);
  color: var(--text-primary);
  text-decoration: none;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.04), 0 2px 8px rgba(0, 0, 0, 0.4);
  transition: background-color var(--transition-smooth), 
              border-color var(--transition-smooth), 
              transform var(--transition-smooth), 
              box-shadow var(--transition-smooth);
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  position: relative;
}

.link-btn:hover {
  background-color: var(--surface-hover);
  border-color: var(--border-hover);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.08), 0 6px 24px rgba(0, 0, 0, 0.6);
  transform: translateY(-1px);
}

.link-btn:active {
  transform: translateY(0) scale(0.995);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.02), 0 1px 4px rgba(0, 0, 0, 0.5);
}

.link-btn:focus-visible {
  outline: none;
  border-color: var(--accent-gold);
  box-shadow: 0 0 0 3px var(--gold-glow), inset 0 1px 0 rgba(255, 255, 255, 0.08);
}

/* Button Elements */
.btn-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  color: var(--text-primary);
  flex-shrink: 0;
  opacity: 0.95;
  transition: opacity 0.2s ease;
}

.link-btn:hover .btn-icon {
  opacity: 1;
  color: var(--accent-gold);
}

.btn-label {
  font-size: 1.02rem;
  font-weight: 400;
  letter-spacing: 0.03em;
  color: var(--text-primary);
  text-align: center;
  flex-grow: 1;
  padding-inline: 12px;
}

.btn-arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  color: var(--text-muted);
  flex-shrink: 0;
  transition: transform var(--transition-smooth), color var(--transition-smooth);
}

.link-btn:hover .btn-arrow {
  transform: translateX(3px);
  color: var(--text-primary);
}

/* Reduced Motion Support */
@media (prefers-reduced-motion: reduce) {
  .link-btn, .btn-arrow, .btn-icon {
    transition: none !important;
    transform: none !important;
  }
}
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(improved_index_html)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(improved_style_css)

print("Successfully updated index.html and style.css with premium UI/UX redesign.")