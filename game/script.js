// Your existing code
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

        // Hangman game logic
        var wordToGuess = ""; // The word to guess
        var guessedLetters = []; // Guessed letters
        var attemptsLeft = 6; // Number of attempts allowed

        // Function to choose a random word
        function chooseWord() {
            var words = ["python", "hangman", "programming", "computer", "game"];
            return words[Math.floor(Math.random() * words.length)];
        }

        // Function to display the word with underscores for unguessed letters
        function displayWord() {
            var display = "";
            for (var i = 0; i < wordToGuess.length; i++) {
                if (guessedLetters.includes(wordToGuess[i])) {
                    display += wordToGuess[i];
                } else {
                    display += "_";
                }
            }
            document.getElementById('word-lines').textContent = display;
        }

        // Function to check the guessed letter
        function checkGuess(letter) {
            if (!guessedLetters.includes(letter)) {
                guessedLetters.push(letter);
                if (!wordToGuess.includes(letter)) {
                    attemptsLeft--;
                }
                displayWord();
                checkGameStatus();
            }
        }

        // Function to check the game status (win or lose)
        function checkGameStatus() {
            if (attemptsLeft === 0) {
                alert('Game over! You ran out of attempts. The word was: ' + wordToGuess);
                resetGame();
            } else if (!displayWord().includes('_')) {
                alert('Congratulations! You guessed the word: ' + wordToGuess);
                resetGame();
            }
        }

        // Function to reset the game
        function resetGame() {
            wordToGuess = chooseWord();
            guessedLetters = [];
            attemptsLeft = 6;
            displayWord();
        }

        // Initialize the game
        wordToGuess = chooseWord();
        displayWord();

        // Add click event listeners to letter buttons
        letterButtons.forEach(function (button) {
            button.addEventListener('click', function () {
                checkGuess(button.textContent.toLowerCase());
            });
        });

    }, 1000); // Adjust the time as needed

});