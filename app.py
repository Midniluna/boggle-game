from flask import Flask, render_template, request, redirect, flash, session
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
    return render_template('initialize-game.html', board = session['board'])

