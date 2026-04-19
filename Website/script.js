document.querySelectorAll('input[type="number"]').forEach(input => {
    input.addEventListener('input', () => {

    if (input.value < 0) {
        input.style.borderColor = '#8bdef5';
    } else {
        input.style.borderColor = '#c1b5b5';
    }
    });
});