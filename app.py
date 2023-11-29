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
    easy_words = ['apple', 'banana', 'orange']
    hard_words = ['elephant', 'giraffe', 'rhinoceros']

    word_list = easy_words if difficulty == 'easy' else hard_words
    return random.choice(word_list)

if __name__ == '__main__':
    app.run(debug=True)