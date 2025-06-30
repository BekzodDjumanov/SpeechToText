document.getElementById('upload-form').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent immediate form submission

  // Show the loading overlay by changing its display property before animation
  const loadingOverlay = document.getElementById('loading-overlay');
  loadingOverlay.style.display = 'flex'; // Set to flex to make it visible

  // Animate the overlay into view using GSAP
  gsap.fromTo(loadingOverlay, 
    { opacity: 0, y: "-300" }, // Initial state (invisible and above)
    {
      opacity: 1, 
      y: "0", 
      duration: 2, 
      ease: 'power2.out',
      onStart: function() {
        // Disable the submit button during the animation to prevent multiple submissions
        document.querySelector('button[type="submit"]').disabled = true;
      },
      onComplete: () => {
        // Re-enable the submit button after animation completes
        document.querySelector('button[type="submit"]').disabled = false;

        // Submit the form
        this.submit(); // Trigger the actual form submission
      }
    }
  );
});
  

const sr = ScrollReveal ({
    distance: '65px',
    duration: 2600,
    delay: 450,
    reset: true,
    once: true
});


sr.reveal('.header', {origin: 'top',reset: false});
sr.reveal('.hero-card', {delay: 500, origin: 'bottom',reset: false});

  