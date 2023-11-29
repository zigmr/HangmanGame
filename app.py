from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game/<difficulty>')
def game(difficulty)
    word = get_word(difficulty)
    return render_template('play.html', difficulty=difficulty, word=word)

@app.route('/check_guess/<word>/<guess>')
def check_guess(word, guess):
    if guess in word:
        return jsonify(result='correct')
    else:
        return jsonify(result='incorrect')

# Demonstrates the use of lists (learned in data structures course)
def get_word(difficulty):
    easy_words = ["apple", "banana", "cat", "dog", "elephant", "fish", "green", "happy",
                 "island", "jacket", "kite", "lemon", "mouse", "nest", "orange", "purple",
                 "queen", "rabbit", "sun", "turtle", "umbrella", "violet", "water", "xylophone",
                 "yellow", "zebra", "air", "bird", "cloud", "dolphin", "egg", "flower", "guitar",
                 "hat", "ice cream", "juice", "key", "laptop", "moon", "notebook", "ocean", "pencil",
                 "quiet", "rose", "star", "tree", "unicorn", "volcano", "window", "xylophone", "zeppelin"]
    hard_words = ["antidisestablishmentarianism", "benevolence", "cacophony", "deoxyribonucleic", "ephemeral",
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

    word_list = easy_words if difficulty == 'easy' else hard_words
    return random.choice(word_list)

if __name__ == '__main__':
    app.run(debug=True)