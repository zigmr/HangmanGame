import random
import time


def select_word(difficulty):
    word_lists = {
        "easy": ["apple", "banana", "cat", "dog", "elephant", "fish", "green", "happy",
                 "island", "jacket", "kite", "lemon", "mouse", "nest", "orange", "purple",
                 "queen", "rabbit", "sun", "turtle", "umbrella", "violet", "water", "xylophone",
                 "yellow", "zebra", "air", "bird", "cloud", "dolphin", "egg", "flower", "guitar",
                 "hat", "icecream", "juice", "key", "laptop", "moon", "notebook", "ocean", "pencil",
                 "quiet", "rose", "star", "tree", "unicorn", "volcano", "window", "xylophone", "zeppelin"
                 ],
        "hard": ["antidisestablishmentarianism", "benevolence", "cacophony", "deoxyribonucleic", "ephemeral",
                 "facetious", "garrulous", "higgledy-piggledy", "idiosyncrasy", "juxtaposition",
                 "kaleidoscopic", "labyrinthine", "mnemonic", "obfuscate", "peculiar",
                 "quintessential", "recalcitrant", "sesquipedalian", "triskaidekaphobia", "ubiquitous",
                 "vexatious", "weltschmerz", "xanthosis", "yurt", "zeitgeist",
                 "aberration", "belligerent", "circumlocution", "disparate", "exacerbate",
                 "flibbertigibbet", "grandiloquent", "hierarchical", "iconoclast", "jingoistic",
                 "kowtow", "lugubrious", "mellifluous", "nepotism", "obfuscation",
                 "peregrinate", "quixotic", "ratiocination", "sesquipedalian", "taciturn",
                 "ubiquity", "verisimilitude", "welter", "xenophobe", "yammer",
                 "zymurgy"]
    }
    return random.choice(word_lists[difficulty])


def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()


def get_user_guess(used_letters):
    while True:
        guess = input("\nEnter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.\n")
            continue

        if guess in used_letters:
            print("You've already guessed that letter. Try again.\n")
            continue

        return guess


def get_hint(word, guessed_letters):
    letters_remaining = [letter for letter in word if letter not in guessed_letters]
    hint = random.choice(letters_remaining)
    print(f"Hint: The word contains the letter '{hint}'.")


def display_hangman(incorrect_guesses):
    hangman_graphics = [
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """
    ]
    print(hangman_graphics[incorrect_guesses])


def choose_difficulty():
    while True:
        difficulty = input("Choose difficulty (easy/hard): ").lower()
        if difficulty in ["easy", "hard"]:
            return difficulty
        else:
            print("Invalid difficulty. Please choose 'easy' or 'hard'.")


def get_player_name():
    return input("Enter your name: ")


def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == "yes"


def update_score(scores, player_name, player_score):
    if player_name not in scores:
        scores[player_name] = []
    scores[player_name].append(player_score)


def save_scores(scores):
    filename = "hangman_scores.txt"
    with open(filename, "w") as file:
        for player_name, player_scores in scores.items():
            file.write(f"{player_name}'s scores: {', '.join(map(str, player_scores))}\n")
    print(f"Scores saved to {filename}.")


def display_top_scores(scores):
    print("\nTop 5 Scores:")
    sorted_scores = sorted(scores.items(), key=lambda x: max(x[1]), reverse=True)[:5]
    for player_name, player_scores in sorted_scores:
        print(f"{player_name}: {max(player_scores)}")

def display_hangman(incorrect_guesses, difficulty):

    if difficulty == 'easy':

        hangman_graphics = [
            """
            -----
            |   |
                |
                |
                |
                |
            ---------
            """,
            """
            -----
            |   |
            O   |
                |
                |
                |
            ---------
            """,
            """
            -----
            |   |
            O   |
            |   |
                |
                |
            ---------
            """,
            """
            -----
            |   |
            O   |
           /|   |
                |
                |
            ---------
            """,
            """
            -----
            |   |
            O   |
           /|\  |
                |
                |
            ---------
            """,
            """
            -----
            |   |
            O   |
           /|\  |
            /   |
                |
            ---------
            """,
            """
            -----
            |   |
            O   |
           /|\  |
           / \  |
                |
            ---------
            """
        ]

    else:
        hangman_graphics = [
            """
            -----
            |   |
                |
                |
                |
                |
            ---------
            """,
            """
            -----
            |   |
            O   |
                |
                |
                |
            ---------
            """,
            """
            -----
            |   |
            O   |
            |   |
                |
                |
            ---------
            """,
            
            """
            -----
            |   |
            O   |
           /|\  |
                |
                |
            ---------
            """,
            
            """
            -----
            |   |
            O   |
           /|\  |
           / \  |
                |
            ---------
            """
        ]

    print(hangman_graphics[incorrect_guesses])


def hangman():
    scores = {}
    
    while True:

        player_name = get_player_name()
        player_score = 0

        difficulty = choose_difficulty()
        selected_word = select_word(difficulty)

        max_attempts = 6 if difficulty == "easy" else 4
        used_letters = []
        incorrect_guesses = 0

        print(f"Welcome to Hangman, {player_name}! Difficulty: {difficulty.capitalize()}\n")
        display_hangman(incorrect_guesses, difficulty)
        
        start_time = time.time()

        while incorrect_guesses < max_attempts:
            

        
            print(display_word(selected_word, used_letters))
            display_hangman(incorrect_guesses)

            if input("Do you want a hint? (yes/no): ").lower() == "yes":
                get_hint(selected_word, used_letters)

            guess = get_user_guess(used_letters)
            used_letters.append(guess)
            
            

            if guess not in selected_word:
                incorrect_guesses += 1
                print(f"Incorrect guess! Attempts remaining: {max_attempts - incorrect_guesses}")
                
            else:
                print("Good guess!")


            current_display = display_word(selected_word, used_letters)
            display_hangman(incorrect_guesses, difficulty)

            if "_" not in current_display:
                end_time = time.time()
                time_taken = end_time - start_time
                print("Congratulations! You've guessed the word in {:.2f} seconds.\n".format(time_taken))
                if difficulty == 'easy':

                    player_score += 1
                else:
                    player_score += 2

                update_score(scores, player_name, player_score)
                break

        if "_" in display_word(selected_word, used_letters):
            print(f"Sorry, you ran out of attempts. The word was: {selected_word}")
            
            

        print(f"Your current score: {player_score}")
        save_scores(scores)
        display_top_scores(scores)

        if not play_again():
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Getting a new word for the next round...\n")


if __name__ == "__main__":
    hangman()

