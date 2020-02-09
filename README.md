Department-app

The basic CRUD application presented as graduation work by Anatolii Krukovych.
[![Build Status](https://travis-ci.com/akrukovich/department-app.svg?branch=master)](https://travis-ci.com/akrukovich/department-app)
[![Coverage Status](https://coveralls.io/repos/github/akrukovich/department-app/badge.svg?branch=feature)](https://coveralls.io/github/akrukovich/department-app?branch=feature)

Requirements
To install and run these examples you need:

Python 3.7+  
virtualenv  
mysql  
git (only to clone this repository)

Install
# clone the repository
$ git clone https://github.com/akrukovich/department-app.git  
$ cd department-app

Create a virtualenv and activate it:

$ python3 -m venv venv   
$ pip install -r requirements.txt

Mysql 

Change app/__init__ app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@127.0.0.1/db_name'


Run

$ export FLASK_APP=run  
$ export FLASK_ENV=development  
$ flask init db 
$ flask init migrate  
$ flask init upgrade  

Create admin user  
$ flask shell  
$ from .models import Employee  
$ from app import db  
$ admin = Employee(email="example@example.com",username="example",password="example",is_admin=True)

$ db.session.add(admin)  
$ db.session.commit()
  

$ flask run  
or gunicorn  
$ gunicorn --bind 0.0.0.0:5000 run_wsgi


Test and coverage

Change tests/util.py app.config.update(SQLALCHEMY_DATABASE_URI='mysql://root:password@localhost/db_name_test')  
$ python manage.py test

Run with coverage report:

$ coverage run -m unittest tests/*.py && coverage html

# open htmlcov/index.html in a browser
