# import os
# import unittest
# # import coverage

# from app.util import create_app
# from flask_script import Manager



# # COV = coverage.coverage(
# #         branch=True,
# #         include='project/*',
# #         omit=['*/__init__.py', '*/config/*']
# #     )
# # COV.start()

# config_name = os.getenv('testing') or 'default'
# app = create_app(config_name)

# manager = Manager(app)

# # migrations


# @manager.command
# def test():
#     """Runs the unit tests without coverage."""
#     tests = unittest.TestLoader().discover('tests')
#     result = unittest.TextTestRunner(verbosity=2).run(tests)
#     if result.wasSuccessful():
#         return 0
#     else:
#         return 1


# # @manager.command
# # def cov():
# #     """Runs the unit tests with coverage."""
# #     tests = unittest.TestLoader().discover('tests')
# #     unittest.TextTestRunner(verbosity=2).run(tests)
# #     COV.stop()
# #     COV.save()
# #     print('Coverage Summary:')
# #     COV.report()
# #     basedir = os.path.abspath(os.path.dirname(__file__))
# #     covdir = os.path.join(basedir, 'tmp/coverage')
# #     COV.html_report(directory=covdir)
# #     print('HTML version: file://%s/index.html' % covdir)
# #     COV.erase()




# if __name__ == '__main__':
#     manager.run()
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
