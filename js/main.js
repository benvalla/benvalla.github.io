(function () {
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      nav.classList.toggle("is-open", !open);
    });
    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        toggle.setAttribute("aria-expanded", "false");
        nav.classList.remove("is-open");
      });
    });
  }

  var nextInput = document.getElementById("form-next");
  if (nextInput && window.location.protocol !== "file:") {
    var path = window.location.pathname || "/";
    var dir = path.replace(/[^/]*$/, "");
    nextInput.value = window.location.origin + dir + "thank-you.html";
  }
})();
