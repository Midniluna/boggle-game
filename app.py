from flask import Flask, render_template, request, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)

app.config['SECRET_KEY'] = "very_secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def start_page():
    if session.get('board'):
        return redirect ('/boggle-game')
    return render_template('home.html')


@app.route('/start', methods=['POST'])
def generate_board():
    new_game = boggle_game.make_board()
    session['board'] = new_game
    return redirect('/boggle-game')

@app.route('/boggle-game')
def start_game():
    if not session.get('board'):
        return redirect('/')
    return render_template('initialize-game.html', board = session['board'])

@app.route('/check-word')
def check_word():
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})
    

@app.route('/final-score', methods=['POST'])
def submit_word():
    score = request.json["score"]
    highscore = session.get("highscore", 0)
    numplays = session.get("numplays", 0)

    session['numplays'] = numplays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokeRecord=score > highscore)

@app.route('/restart')
def restart_game():
    session.pop('board', default=None)
    return redirect('/')
