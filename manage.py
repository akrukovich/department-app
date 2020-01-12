import os
import unittest

from app.util import create_app
from flask_script import Manager


from flask_script import Manager
from tests.util import create_app

config_name = os.getenv('testing') or 'default'
app = create_app(config_name)

manager = Manager(app)

@manager.command
def test():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()

