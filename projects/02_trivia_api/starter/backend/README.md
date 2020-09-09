# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

DOCUMENTATION
-------------

This is an API that powers a Trivia game. It returns resources such as fromatted categories and questions for the frontend to handle the quizze game logic.

+ Base URL: The base url of the API Server is http://localhost:5000
It is the local machine's IP Address. That is because the API is not hosted yet on a server available through the Internet.

+ Autentication: This application doesn't use authentication process.

+ Endpoints:

CATEGORIES
----------

GET '/api/categories'
GET '/api/categories/<int:id>/questions

GET '/api/categories'
- Result: Fetches a dictionary of categories in which the keys are the ids and the values are the corresponding strings of the categories
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

QUESTIONS
---------

GET '/api/questions'
DELETE '/api/questions/<int:id>'
POST '/api/questions'
POST '/api/questions/search'
POST '/api/quizzes'

GET '/api/questions'
- Result: Fetches a dictionary of questions in which the keys are the ids and the values are the questions strings
- Request Arguments: None
- Returns: An object composed of all categories, the status message of the response, the total number of questions, the questions objects composed of keys question, answer, category, difficulty and their corresponding values. 

{
    "categories": {
        "1": "web",
        "2": "football",
        "3": "animals"
    },
    "current_category": null,
    "questions": [
        {
            "answer": "1990",
            "category": "web",
            "difficulty": 3,
            "id": 1,
            "question": "When was http the foundation of the internet?"
        },
        {
            "answer": "Ronaldinho",
            "category": "football",
            "difficulty": 3,
            "id": 2,
            "question": "Who the most famous football player?"
        },
        {
            "answer": "Cheeta",
            "category": "animals",
            "difficulty": 2,
            "id": 3,
            "question": "Which animal is the fastest of the world"
        }
    ],
    "success": true,
    "total_questions": 3
}

DELETE '/api/questions/<int:id>'
- Result: Deletes a specific question with its id given as parameter in the path
- Request Arguments: Question id
- Returns: The status message of the deletion operation and the id of the deleted question

{
    "question_id": 2,
    "success": true
}

POST '/api/questions'
- Result: Creates a question with a question string, the answer of the question, the category of the question and the difficulty of the question
- Request argument: a json object with keys question, answer, category, difficulty and the corresponding values.
- Returns: The status message of the response and the id of created question

{
    "question_id": 8,
    "success": true
}

POST '/api/questions/search'
- Result: Fetches the questions in which a search term is included in questions strings
- Request argument: a json object with search term key and corresponding value
- Returns: The status message of the response and the formatted questions corresponding to the search term

{
    "questions": {
            "answer": "Cheeta",
            "category": "animals",
            "difficulty": 2,
            "id": 3,
            "question": "Which animal is the fastest of the world"
        },
    "success": true
}

POST '/api/quizzes'
- Result: Takes a category and previous question parameters 
  and returns a random questions within the given category that is not one of the previous questions
- Request argument: The category object of the questions the display with keys id, category and corresponding values and the list of previous displayed questions
- Returns: A question object with keys question string, answer, category, difficulty and corresponding values

{
    'question': {
            "answer": "1990",
            "category": "web",
            "difficulty": 3,
            "id": 1,
            "question": "When was http the foundation of the internet?"
        }
}


```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```