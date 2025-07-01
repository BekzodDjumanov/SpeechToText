// library for movement
const sr = ScrollReveal ({
    distance: '65px',
    duration: 2600,
    delay: 450,
    reset: true,
    once: true
});

sr.reveal('.header', {origin: 'top',reset: false});
sr.reveal('.result', {origin: 'top', result: false});