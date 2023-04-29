from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    class GenerateBoard(TestCase):
        def check_redirect(self):
            with app.test_client() as client:
                res = client.get('/start')
                self.assertEqual(res.status_code, 302)
                self.assertEqual(res.location, 'http://localhost/boggle-game')
                