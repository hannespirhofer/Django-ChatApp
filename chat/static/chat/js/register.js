document.addEventListener("DOMContentLoaded", () => {
    const usernameField = document.getElementById("username");
    const firstnameField = document.getElementById("firstname");
    const passwordField = document.getElementById("password");
    const passwordRepeatField = document.getElementById("password_repeat");
    const passwordMatchMessage = document.getElementById("password_match_msg");
    const registerButton = document.getElementById("register");
    passwordMatchMessage.innerHTML = "";

    function toggleButtonState() {
        if (usernameField.value.trim() && firstnameField.value.trim() && passwordField.value.trim() && passwordRepeatField.value.trim()) {
            if (passwordField.value.trim() === passwordRepeatField.value.trim()) {
                registerButton.disabled = false;
            }
        } else {
            registerButton.disabled = true;
        }
    }

    function onCheckPassword() {
        const password = passwordField.value.trim();
        const passwordRepeat = passwordRepeatField.value.trim();

        if (password && passwordRepeat) {
            if (password === passwordRepeat) {
                passwordMatchMessage.innerHTML = "";
            } else {
                passwordMatchMessage.innerHTML = "Passwords must match.";
            }
        } else {
            passwordMatchMessage.innerHTML = "";
        }
    }

    function onUsernameInput() {
        let username = usernameField.value.trim();
        usernameField.value = username.toLowerCase();
    }

    usernameField.addEventListener("input", toggleButtonState);
    usernameField.addEventListener("input", onUsernameInput);
    firstnameField.addEventListener("input", toggleButtonState);
    passwordRepeatField.addEventListener("input", toggleButtonState);
    passwordField.addEventListener("input", toggleButtonState);

    passwordRepeatField.addEventListener("input", onCheckPassword);

    //Initial check in case there are prefilled values from the browser
    toggleButtonState();
});