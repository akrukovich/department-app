Department-app

The basic CRUD application presented as graduation work by Anatolii Krukovych.
[![Build Status](https://travis-ci.com/akrukovich/department-app.svg?branch=master)](https://travis-ci.com/akrukovich/department-app)
[![Coverage Status](https://coveralls.io/repos/github/akrukovich/department-app/badge.svg?branch=feature)](https://coveralls.io/github/akrukovich/department-app?branch=feature)

Requirements
To install and run these examples you need:

Python 3.7+
virtualenv 
git (only to clone this repository)

Install
# clone the repository
$ git clone https://github.com/akrukovich/department-app.git
$ cd department-app
# checkout the correct version

Create a virtualenv and activate it:

$ python3 -m venv venv
$ . venv/bin/activate
Or on Windows cmd:

$ py -3 -m venv venv
$ venv\Scripts\activate.bat
Install Flaskr:

$ pip install -r requirements.txt

Run
$ export FLASK_APP=run
$ export FLASK_ENV=development
$ flask init db
$ flask init migrate
$ flask init upgrade
$ flask run

Test and coverage
$ python manage.py test

Run with coverage report:

$ coverage run -m unittest tests/*.py && coverage html

# open htmlcov/index.html in a browser
