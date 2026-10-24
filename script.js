const GA_MEASUREMENT_ID = "";

if (GA_MEASUREMENT_ID && GA_MEASUREMENT_ID.trim() !== "") {
  const script = document.createElement("script");
  script.async = true;
  script.src = `https://www.googletagmanager.com/gtag/js?id=${GA_MEASUREMENT_ID}`;
  document.head.appendChild(script);

  window.dataLayer = window.dataLayer || [];
  function gtag() {
    dataLayer.push(arguments);
  }
  gtag("js", new Date());
  gtag("config", GA_MEASUREMENT_ID);

  document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".link-btn");
    buttons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const linkName = btn.getAttribute("data-link-name");
        if (linkName && typeof gtag === "function") {
          gtag("event", "outbound_click", {
            link_name: linkName
          });
        }
      });
    });
  });
}
