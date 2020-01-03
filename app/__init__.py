# app/__init__.py
# third-party imports
from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_bootstrap import Bootstrap
from flask_script import Manager
from loggers import get_logger
from config import app_config

# db variable initialization
db = SQLAlchemy()

# LoginManager variable initialization.
login_manager = LoginManager()
# Logger object initialization.
logger = get_logger(__name__)


def create_app(config_name):
    """Create Flask application

    Create Flask application with configuration provided by config_name variable.
    Furthermore, this function create database migrations and handle 403,404,500 errors.
    Args:
        config_name: configuration variable that configure executing mod.

    Returns: Flask application.

    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Ak12345678@127.0.0.1/dep_db_test'
    app.config['SECRET_KEY'] = 'asdasdasdasd'

    Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand, compare_type=True)

    from app import models

    # Each blueprint object has imported  and registered. For the admin blueprint,
    # url prefix /admin is added. This means that all the views for this blueprint will be accessed
    # in the browser with the url prefix admin.

    from app.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    @app.errorhandler(403)
    def forbidden(error):
        logger.error('403 Error occurred')

        return render_template('errors/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        logger.error('404 Error occurred')

        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        logger.error('500 Error occurred')

        return render_template('errors/500.html', title='Server Error'), 500

    @app.route('/500')
    def error():
        abort(500)

    return app

