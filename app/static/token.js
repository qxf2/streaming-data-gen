document.addEventListener('DOMContentLoaded', function () {
const form = document.getElementById('register-form');
form.addEventListener('submit', async function (event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    console.log('Register form submitted');
    console.log('Username:', username);
    console.log('Password:', password);

    try {
        const response = await fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });

        console.log('Response status:', response.status);
        console.log('Response OK:', response.ok);

        const message = document.getElementById('register-message');
        if (response.ok) {
            const data = await response.json();
            message.textContent = "Registration successful! Login with the registered credentials to generate a token.";
            console.log('Registration successful:', data);
            form.reset();

            setTimeout(function () {
                message.textContent = '';
            }, 5000);


            setTimeout(function () {
                showSection('login-section');
            }, 2000);
        } else {
            const contentType = response.headers.get('content-type');
            if (contentType && contentType.indexOf('application/json') !== -1) {
                const errorData = await response.json();
                message.textContent = `Registration failed: ${errorData.detail}`;
                console.log('Registration failed:', errorData.detail);
            } else {
                const errorText = await response.text();
                message.textContent = `Registration failed: ${errorText}`;
                console.log('Registration failed:', errorText);
            }
        }
    } catch (error) {
        document.getElementById('register-message').textContent = `Error: ${error}`;
        console.log('Error:', error);
    }
});
});
