document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('login-form');
    const loginMessage = document.getElementById('login-message');
    const modalTokenMessage = document.getElementById('modal-token-message');
    const copyTokenButton = document.getElementById('copyTokenButton');

    loginForm.addEventListener('submit', async function (event) {
        event.preventDefault();
        const username = document.getElementById('login-username').value;
        const password = document.getElementById('login-password').value;

        try {
            const response = await fetch('/token', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({ username, password }),
            });

            console.log('Response status:', response.status);
            console.log('Response OK:', response.ok);

            if (response.ok) {
                const data = await response.json();
                modalTokenMessage.textContent = `${data.access_token}`;
                console.log('Token generated:', data.access_token);
                openModal('tokenModal');
                loginForm.reset();

                loginMessage.textContent = '';

                copyTokenButton.addEventListener('click', function () {
                    copyToClipboard(data.access_token);
                });
            } else {
                const contentType = response.headers.get('content-type');
                if (contentType && contentType.indexOf('application/json') !== -1) {
                    const errorData = await response.json();
                    loginMessage.textContent = `Login failed: ${errorData.detail}`;
                    console.log('Login failed:', errorData.detail);
                } else {
                    const errorText = await response.text();
                    loginMessage.textContent = `Login failed: ${errorText}`;
                    console.log('Login failed:', errorText);
                }
            }
        } catch (error) {
            loginMessage.textContent = `Error: ${error}`;
            console.log('Error:', error);
        }
    });
});


function copyToClipboard(text) {
    const tempInput = document.createElement('input');
    tempInput.style.position = 'absolute';
    tempInput.style.left = '-9999px';
    tempInput.value = text;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand('copy');
    document.body.removeChild(tempInput);
    notification.classList.add('show');
    setTimeout(function () {
        notification.classList.remove('show');
    }, 2000); 
}