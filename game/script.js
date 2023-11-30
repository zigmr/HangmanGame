function redirectBtn() {
    var URL = "play.html";

    window.location.href = URL;
}

document.addEventListener("DOMContentLoaded", function () {
    // Simulate loading time (you can replace this with actual loading logic)
    setTimeout(function () {
        // Hide the loading animation
        document.querySelector('.loader-wrapper').style.display = 'none';

        // Play the pop sound
        document.getElementById('popSound').play();

        // Show the content
        document.getElementById('content').style.display = 'block';

        // Show the letters
        document.getElementById('letter-buttons').style.display = 'block';

        // Play background music
        document.getElementById('backgroundMusic').play();

        // Add click sound to letter buttons
        var letterButtons = document.querySelectorAll('.letter-button');
        letterButtons.forEach(function (button) {
            button.addEventListener('click', function () {
                document.getElementById('clickSound').play();
            });
        });
    }, 1000); // Adjust the time as needed
});

