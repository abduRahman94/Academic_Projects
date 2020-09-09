import os
from flask import Flask, request, abort, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  

  def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = [question.format() for question in selection]
    current_questions = questions[start:end]
    return current_questions
    
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  cors = CORS(app, resources={"/api/*": {"origins":"*"}})

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow','Content-Type, Authorization')
    response.headers.add('Access-Control-Methods','GET, POST, PATCH, DELETE, OPTIONS')
    return response

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/api/categories', methods=['GET'])
  def get_categories():
    selection = Category.query.order_by(Category.id).all()
    categories = {category.id: category.type for category in selection}
    return jsonify({
      'success': True,
      'categories': categories
      })

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories.

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/api/questions', methods=['GET'])
  def get_questions():
    body = request.get_json()
    question_selection = Question.query.all()
    category_selection = Category.query.all()
    categories = {category.id: category.type for category in category_selection}
    current_questions = paginate_questions(request, question_selection)
    number_questions = len(question_selection)
    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': number_questions,
      'current_category': None,
      'categories': categories
    })
    

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/api/questions/<int:id>', methods=['DELETE'])
  def delete_question(id):
    try:
      question = Question.query.get(id)
      question.delete()
      return jsonify({
        'success': True,
        'question_id': question.id
        })
    except:
        abort(404)


  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/api/questions', methods=['POST'])
  def add_question():
    body = request.get_json()
    
    try:
      question = body.get('question')
      answer = body.get('answer')
      category = body.get('category')
      difficulty = int(body.get('difficulty'))
      
      myQuestion = Question(question=question,answer=answer,category=category,difficulty=difficulty)
      myQuestion.insert()
      
      return jsonify({
        'success': True,
        'question_id': myQuestion.id
      })
    except:
      abort(400)



  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/api/questions/search', methods=['POST'])
  def search_question():
    body = request.get_json()
    
    try:
      
      search_term = body.get('searchTerm')
      questions = Question.query.filter(Question.question.ilike("%" + search_term + "%")).all()
      results = [question.format() for question in questions]
      return jsonify({
          'success': True,
          'questions': results
      })
    
    except:
      abort(404)

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/api/categories/<int:id>/questions', methods=['GET'])
  def get_questionByCateg(id):
   
      categories = Category.query.filter(Category.id==id).all()
      test_category = Category.query.get(id)
      category = [category.format() for category in categories]
      questions = Question.query.filter_by(category=test_category.type).all()
      results = [question.format() for question in questions]
      return jsonify({
            'success': True,
            'questions': results,
            'total_questions': len(questions),
            'current_category': category
          })



  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/api/quizzes', methods=['POST']) #For this endpoint, inspired in a mentor guidance
  def get_quizzQuestions():
    body = request.get_json()
    
  
    try:
      previousQuestions = body.get('previous_questions', [])
      quizCategory = body.get('quiz_category', None)
      id_cateogry = int(quizCategory['id']) + 1
      if quizCategory:
        if quizCategory['id']==0:
          questions = Question.query.all()
        else:
          questions = Question.query.filter(Question.category==quizCategory['type']).all()
      
      if not questions:
        return abort(422)
      result = []
      for question in questions:
        if question.id not in previousQuestions:
          result.append(question.format())
      if len(result) !=0:
        data = random.choice(result)
        return jsonify({
          'question': data
        })
      else:
        return jsonify({
          'question': False
        })
    except:
      abort(404)


  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': 'Resource not found'
    }), 404
  
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      'success': False,
      'error': 400,
      'message': 'Bad client request'
    }), 400
  
  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message': 'Request unprocessable'
    }), 422

  @app.errorhandler(500)
  def internal_error(error):
    return jsonify({
      'success': False,
      'error': 500,
      'message': 'Internal error'
    }), 500
  
  
  return app

    
