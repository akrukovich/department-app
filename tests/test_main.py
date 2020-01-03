from tests.test_models import TestModels

import unittest

def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestModels())
    return test_suite

if __name__ == '__main__':
   suite = create_suite()

   runner=unittest.TextTestRunner()
   runner.run(suite)