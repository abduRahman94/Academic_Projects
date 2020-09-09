import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}@{}/{}".format('abdou:passer','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_getAllCategories(self):
        res = self.client().get('/api/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['categories'], '')

    def test_getAllQuestions(self):
        res = self.client().get('/api/questions')
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['current_category'])
    
    def test_deleteQuestion(self):
        res = self.client().delete('/api/questions/1')
        data = json.loads(res.data)
        self.assertEqual(data['question_id'], 1)
        self.assertNotEqual(data['success'], True)

    def test_insertQuestion(self):
        res = self.client().post('/api/questions', json={'question':'What book is the most valuable on earth ?', 'answer':'The Quran','category':'knowledge','difficulty':'1'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['question_id'], '')
    
    def test_searchQuestion(self):
        res = self.client().post('/api/questions/search', json={'searchTerm':'fastest'})
        data = json.loads(res.data)
        self.assertNotEqual(data['questions'], '')
        self.assertEqual(res.status_code, 404)

    def test_getCategoryQuestions(self):
        res = self.client().get('/api/categories/1/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertLess(data['total_questions'], 0)

    def test_quizzQuestions(self):
        res = self.client().post('/api/quizzes', json={'previous_questions':[], 'quiz_category':{'type':'web','id':'1'}})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['question'], '')






# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()