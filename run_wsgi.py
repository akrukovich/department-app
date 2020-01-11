import os


# import flask app but need to call it "application" for WSGI to work
from app import create_app
config_name = os.getenv('production') or 'default'
application = create_app(config_name)
if __name__ == '__main__':
    # logger = logging.getLogger(__name__)
    application.run()
