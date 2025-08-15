document
  .getElementById("upload-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const loadingOverlay = document.getElementById("loading-overlay");
    loadingOverlay.style.display = "flex"; // set to flex to make it visible

    // GSAP animation
    gsap.fromTo(
      loadingOverlay,
      { opacity: 0, y: "-300" },
      {
        opacity: 1,
        y: "0",
        duration: 2,
        ease: "power2.out",
        onStart: function () {
          // prevent submitting multiple requests
          document.querySelector('button[type="submit"]').disabled = true;
        },
        onComplete: () => {
          // re-enable inbound requests
          document.querySelector('button[type="submit"]').disabled = false;

          this.submit(); // trigger form submission
        },
      }
    );
  });

document.querySelector(".dark-light-btn").addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
});

// library for movement
const sr = ScrollReveal({
  distance: "65px",
  duration: 2600,
  delay: 450,
  reset: true,
  once: true,
});
