document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('register-form');
    form.addEventListener('submit', async function (event) {
        event.preventDefault();

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        const response = await fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });

        const message = document.getElementById('register-message');
        if (response.ok) {
            message.textContent = 'Registration successful!';
        } else {
            const errorData = await response.json();
            message.textContent = `Registration failed: ${errorData.detail}`;
        }
    });
});
