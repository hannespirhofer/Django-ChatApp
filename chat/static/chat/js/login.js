document.addEventListener("DOMContentLoaded", () => {
    const usernameField = document.getElementById("username");
    const passwordField = document.getElementById("password");
    const loginButton = document.getElementById("submit");

    function toggleButtonState() {
        if (usernameField.value.trim() && passwordField.value.trim()) {
            loginButton.disabled = false;
        } else {
            loginButton.disabled = true;
        }
    }

    usernameField.addEventListener("input", toggleButtonState);
    passwordField.addEventListener("input", toggleButtonState);

    //Initial check in case there are prefilled values from the browser
    toggleButtonState();
});