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

        var wrongSoundElement = document.getElementById('wrongSound');

        wrongSoundElement.volume = 0.2;

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
            var words = ["apple", "banana", "cat", "dog", "elephant", "fish", "green", "happy",
            "island", "jacket", "kite", "lemon", "mouse", "nest", "orange", "purple",
            "queen", "rabbit", "sun", "turtle", "umbrella", "violet", "water", "xylophone",
            "yellow", "zebra", "air", "bird", "cloud", "dolphin", "egg", "flower", "guitar",
            "hat", "ice cream", "juice", "key", "laptop", "moon", "notebook", "ocean", "pencil",
            "quiet", "rose", "star", "tree", "unicorn", "volcano", "window", "xylophone", "zeppelin"];
            return words[Math.floor(Math.random() * words.length)];
        }

        // Function to display the word with underscores for unguessed letters
        function displayWord() {
            var display = "";
            for (var i = 0; i < wordToGuess.length; i++) {
                if (wordToGuess[i] === " ") {
                    display += " ";  // Keep spaces as they are
                } else if (guessedLetters.includes(wordToGuess[i])) {
                    display += wordToGuess[i];
                } else {
                    display += " _ ";
                }
            }
            document.getElementById('word-lines').textContent = display;
            return display;  // Return the display string
        }

        // Function to display messages on the screen
        function displayMessage(message) {
            var messageBox = document.getElementById('message-box');
            messageBox.textContent = message;

            // Optionally, you can add a timeout to clear the message after a few seconds
            setTimeout(function () {
                messageBox.textContent = '';
            }, 3000); // Adjust the time as needed (3000 milliseconds = 3 seconds)
        }

        // Function to check the guessed letter
        function checkGuess(letter) {
            if (!guessedLetters.includes(letter)) {
                guessedLetters.push(letter);
                if (!wordToGuess.includes(letter)) {
                    attemptsLeft--;
                    // Play the wrong guess sound
                    document.getElementById('wrongSound').play();
                }
                displayWord();
                checkGameStatus();
            }
        }

        // Function to check the game status (win or lose)
    function checkGameStatus() {
        var display = displayWord();  // Get the current display string

        if (attemptsLeft === 0) {
            displayMessage('Game over! You ran out of attempts. The word was: ' + wordToGuess);
            showPlayAgainButton();
        } else if (!display.includes('_')) {
            document.getElementById('correctSound').play();
            
            displayMessage('Congratulations! You guessed the word: ' + wordToGuess);
            showPlayAgainButton();
        }
    }

        // Function to show the play again button
    function showPlayAgainButton() {
        var playAgainButton = document.getElementById('playAgainButton');
        playAgainButton.style.display = 'block';

        // Hide the letters
        document.getElementById('letter-buttons').style.display = 'none';

        // Clear the word lines
        document.getElementById('word-lines').textContent = '';
    }

    // Function to hide the play again button
    function hidePlayAgainButton() {
        var playAgainButton = document.getElementById('playAgainButton');
        playAgainButton.style.display = 'none';
    }

    // Function to play again
    function playAgain() {
        hidePlayAgainButton();

        // Show the letters
        document.getElementById('letter-buttons').style.display = 'block';

        // Reset the game
        resetGame();
    }

    // Function to reset the game
    function resetGame() {
        wordToGuess = chooseWord();
        guessedLetters = [];
        attemptsLeft = 6;
        displayWord();
    }

    // Add click event listener to the play again button
    var playAgainButton = document.getElementById('playAgainButton');
    playAgainButton.addEventListener('click', playAgain);

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
