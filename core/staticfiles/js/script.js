document.addEventListener('DOMContentLoaded', function () {

    const passwordInput = document.getElementById('password');
    const passwordToggle = document.getElementById('passwordToggle');
    const eyeIcon = passwordToggle.querySelector('.eye-icon');

    passwordToggle.addEventListener('click', function () {

        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            eyeIcon.classList.add('show-password');
        } else {
            passwordInput.type = 'password';
            eyeIcon.classList.remove('show-password');
        }

    });

});