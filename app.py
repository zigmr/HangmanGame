from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game/easy")
def hangman():
    return render_template("game/easy.html")

@app.route("/get_word", methods=["POST"])
def get_word():
    words = ["apple", "banana", "cat", "dog", "elephant", "fish", "green", "happy",
                 "island", "jacket", "kite", "lemon", "mouse", "nest", "orange", "purple",
                 "queen", "rabbit", "sun", "turtle", "umbrella", "violet", "water", "xylophone",
                 "yellow", "zebra", "air", "bird", "cloud", "dolphin", "egg", "flower", "guitar",
                 "hat", "ice cream", "juice", "key", "laptop", "moon", "notebook", "ocean", "pencil",
                 "quiet", "rose", "star", "tree", "unicorn", "volcano", "window", "xylophone", "zeppelin"]
    word = random.choice(words)
    return jsonify({"word": word})

if __name__ == "__main__":
    app.run(debug=True)