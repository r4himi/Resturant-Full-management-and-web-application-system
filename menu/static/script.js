document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById('contactForm');

    const nameInput = document.getElementById('nameInput');
    const emailInput = document.getElementById('emailInput');
    const messageInput = document.getElementById('messageInput');

    const nameError = document.getElementById('nameError');
    const emailError = document.getElementById('emailError');
    const messageError = document.getElementById('messageError');

    if (!form) return;

    function setError(el, msg) {
        if (el) el.textContent = msg;
    }

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        // clear errors
        setError(nameError, "");
        setError(emailError, "");
        setError(messageError, "");

        let isValid = true;

        // NAME
        if (!nameInput.value.trim()) {
            setError(nameError, "Name is required");
            isValid = false;
        }

        // EMAIL
        const emailValue = emailInput.value.trim();
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailValue) {
            setError(emailError, "Email is required");
            isValid = false;
        } else if (!emailPattern.test(emailValue)) {
            setError(emailError, "Enter a valid email address");
            isValid = false;
        }

        // MESSAGE
        if (!messageInput.value.trim()) {
            setError(messageError, "Message is required");
            isValid = false;
        }

        // SUCCESS
        if (isValid) {
            alert("Form submitted successfully!");
            form.reset();
        }
    });

    

});