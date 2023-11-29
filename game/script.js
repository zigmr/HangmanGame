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

        // Play background music
        document.getElementById('backgroundMusic').play();
    }, 1000); // Adjust the time as needed
});