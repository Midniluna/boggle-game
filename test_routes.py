from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    # class GenerateBoard(TestCase):

    def test_valid_word(self):
        with app.test_client() as client:
             with client.session_transaction() as sess:
                sess['board'] = [["D", "O", "G", "G", "S"], 
                                 ["D", "O", "G", "G", "S"], 
                                 ["D", "O", "G", "G", "S"], 
                                 ["D", "W", "G", "B", "A"], 
                                 ["D", "O", "G", "G", "S"]]
        response = client.get('/check-word?word=dog')
        self.assertEqual(response.json['result'], 'ok')
        
    def test_check_session(self):
        with app.test_client() as client:
            client.post('/start')
            response = client.get('/boggle-game')
            self.assertIn('board', session)

    def test_redirect(self):
        with app.test_client() as client:
            client.post('/start')
            res = client.get('/')
            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, '/boggle-game')

    def test_reset(self):
        with app.test_client() as client:
            client.get('/reset')