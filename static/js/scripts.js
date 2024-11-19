// Function to handle the dismissal of the alert box
function dismissAlert(alertBox) {
    // Add a fade-out class to the alert box
    alertBox.classList.add('fade-out');

    // After the fade-out animation (500ms), hide the alert box
    setTimeout(function () {
        alertBox.style.display = 'none';
    }, 500); // 500ms corresponds to the duration of the fade-out transition
}