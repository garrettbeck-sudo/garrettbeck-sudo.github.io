(function () {
  const root = document.documentElement;
  const toggle = document.querySelector(".theme-toggle");
  const storedTheme = localStorage.getItem("garrett-theme");
  const initialTheme = storedTheme || "dark";

  function setTheme(theme, persist) {
    root.setAttribute("data-theme", theme);
    root.setAttribute("data-theme-user", persist ? "true" : "false");
    if (toggle) {
      const isDark = theme === "dark";
      toggle.setAttribute("aria-pressed", String(isDark));
      toggle.setAttribute("aria-label", isDark ? "Switch to light theme" : "Switch to dark theme");
    }
    if (persist) localStorage.setItem("garrett-theme", theme);
  }

  setTheme(initialTheme, Boolean(storedTheme));

  if (toggle) {
    toggle.addEventListener("click", function () {
      setTheme(root.getAttribute("data-theme") === "dark" ? "light" : "dark", true);
    });
  }
})();