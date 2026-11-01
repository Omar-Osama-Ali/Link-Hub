(() => {
  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  /*
   * Optional analytics. Leave blank if you do not use Google Analytics.
   * If configured, analytics are not loaded until the visitor explicitly opts in.
   */
  const GA_MEASUREMENT_ID = "";
  const consentKey = "omar-linkhub-analytics-consent";
  const notice = document.getElementById("cookie-notice");
  const accept = document.getElementById("cookie-accept");
  const reject = document.getElementById("cookie-reject");

  function loadAnalytics() {
    if (!GA_MEASUREMENT_ID || window.__omarAnalyticsLoaded) return;
    window.__omarAnalyticsLoaded = true;
    const script = document.createElement("script");
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(GA_MEASUREMENT_ID)}`;
    document.head.appendChild(script);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", GA_MEASUREMENT_ID, { anonymize_ip: true });
    document.querySelectorAll("[data-link-name]").forEach((link) => {
      link.addEventListener("click", () => {
        window.gtag("event", "outbound_click", { link_name: link.dataset.linkName || "unknown" });
      });
    });
  }

  if (GA_MEASUREMENT_ID && notice) {
    const savedConsent = localStorage.getItem(consentKey);
    if (savedConsent === "accepted") loadAnalytics();
    else if (!savedConsent) notice.hidden = false;
    if (accept) accept.addEventListener("click", () => {
      localStorage.setItem(consentKey, "accepted");
      notice.hidden = true;
      loadAnalytics();
    });
    if (reject) reject.addEventListener("click", () => {
      localStorage.setItem(consentKey, "rejected");
      notice.hidden = true;
    });
  }

  // Lightweight pointer highlight on the 3D art is deliberately avoided:
  // the sculpture is CSS-based, responsive, and does not follow the cursor.
})();
