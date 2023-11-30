from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

word_lists = {
    "easy": ["apple", "banana", "cat", "dog", "elephant", "fish", "green", "happy",
                 "island", "jacket", "kite", "lemon", "mouse", "nest", "orange", "purple",
                 "queen", "rabbit", "sun", "turtle", "umbrella", "violet", "water", "xylophone",
                 "yellow", "zebra", "air", "bird", "cloud", "dolphin", "egg", "flower", "guitar",
                 "hat", "ice cream", "juice", "key", "laptop", "moon", "notebook", "ocean", "pencil",
                 "quiet", "rose", "star", "tree", "unicorn", "volcano", "window", "xylophone", "zeppelin"],
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_word/<difficulty>', methods=['GET'])
def get_word(difficulty):
    word = select_word(difficulty)
    return jsonify({'word': word})

def select_word(difficulty):
    return random.choice(word_lists[difficulty])

if __name__ == '__main__':
    app.run(debug=True)