// Function to handle the dismissal of the alert box
function dismissAlert(alertBox) {
    // Add a fade-out class to the alert box
    alertBox.classList.add('fade-out');

    // After the fade-out animation (500ms), hide the alert box
    setTimeout(function () {
        alertBox.style.display = 'none';
    }, 500); // 500ms corresponds to the duration of the fade-out transition
}

// Function to listen for keyboard inputs and detect the Konami code
function listenForKonamiCode() {
    const konamiCode = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65]; // Up, Up, Down, Down, Left, Right, Left, Right, B, A
    let konamiCodePosition = 0;

    document.addEventListener('keydown', function (event) {
        if (event.keyCode === konamiCode[konamiCodePosition]) {
            konamiCodePosition++;
            if (konamiCodePosition === konamiCode.length) {
                // Konami code successfully entered
                activateKonamiCode();
                konamiCodePosition = 0;
            }
        } else {
            konamiCodePosition = 0;
        }
    });
}

// Function to execute when the Konami code is entered
function activateKonamiCode() {
    window.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', '_blank');
}

// Initialize the Konami code listener
listenForKonamiCode();