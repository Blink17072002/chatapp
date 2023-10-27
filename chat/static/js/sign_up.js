const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

document.addEventListener('DOMContentLoaded', function () {
    const loginPasswordInput = document.getElementById('loginPassword');
    const showLoginPasswordIcon = document.querySelector('.show-login-password');

    showLoginPasswordIcon.addEventListener('click', () => {
        if (loginPasswordInput.type === 'password') {
            loginPasswordInput.type = 'text';
            showLoginPasswordIcon.classList.replace('fa-eye-slash', 'fa-eye');
        } else {
            loginPasswordInput.type = 'password';
            showLoginPasswordIcon.classList.replace('fa-eye', 'fa-eye-slash');
        }
    });

    const signupPasswordInput = document.getElementById('signupPassword');
    const showSignupPasswordIcon = document.querySelector('.show-signup-password');

    showSignupPasswordIcon.addEventListener('click', () => {
        if (signupPasswordInput.type === 'password') {
            signupPasswordInput.type = 'text';
            showSignupPasswordIcon.classList.replace('fa-eye-slash', 'fa-eye');
        } else {
            signupPasswordInput.type = 'password';
            showSignupPasswordIcon.classList.replace('fa-eye', 'fa-eye-slash');
        }
    });

    const confirmInput = document.getElementById('confirmPassword');
    const showConfirmPasswordIcon = document.querySelector('.show-confirm-password');

    showConfirmPasswordIcon.addEventListener('click', () => {
        if (confirmInput.type === 'password') {
            confirmInput.type = 'text';
            showConfirmPasswordIcon.classList.replace('fa-eye-slash', 'fa-eye');
        } else {
            confirmInput.type = 'password';
            showConfirmPasswordIcon.classList.replace('fa-eye', 'fa-eye-slash');
        }
    });
});
