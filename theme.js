// Theme toggle. The initial theme is set by an inline snippet in <head> so the
// page never flashes the wrong one; this only wires up the button.
(function () {
  var root = document.documentElement;

  function current() {
    var set = root.getAttribute("data-theme");
    if (set) return set;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function apply(mode) {
    root.setAttribute("data-theme", mode);
    try { localStorage.setItem("theme", mode); } catch (e) {}
    var b = document.querySelector(".theme");
    if (b) b.setAttribute("aria-label", mode === "dark" ? "Switch to light theme" : "Switch to dark theme");
  }

  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest(".theme");
    if (!b) return;
    apply(current() === "dark" ? "light" : "dark");
  });

  // Follow the system until the viewer picks a side themselves.
  try {
    window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function (ev) {
      var saved = null;
      try { saved = localStorage.getItem("theme"); } catch (e) {}
      if (!saved) root.setAttribute("data-theme", ev.matches ? "dark" : "light");
    });
  } catch (e) {}

  var b = document.querySelector(".theme");
  if (b) b.setAttribute("aria-label", current() === "dark" ? "Switch to light theme" : "Switch to dark theme");
})();
