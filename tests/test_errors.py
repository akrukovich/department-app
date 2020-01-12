import unittest
from flask import abort
from tests.util import TestBase
from loggers import get_logger

logger = get_logger(__name__)


class TestErrorPages(TestBase):
    """Class of errors testing.
    """

    def test_403_forbidden(self):
        """403 error test.
        Test 403 error page.
        Returns:
            None
        """

        @self.app.route('/403')
        def forbidden_error():
            abort(403)

        response = self.client.get('/403')
        self.assertEqual(response.status_code, 403)
        self.assertTrue("403 Error".encode() in response.data)
        logger.info(f'403 forbidden status: {response.status_code}. Test is done.')

    def test_404_not_found(self):
        """404 error test.
        Test 404 error page.
        Returns:
                None
        """
        response = self.client.get('/empty')
        self.assertEqual(response.status_code, 404)
        self.assertTrue("404 Error".encode() in response.data)
        logger.info(f"Access to /empty is denied."
                    f"It doesnt exist, status: {response.status_code}. Test is done")

    def test_500_internal_server_error(self):
        """500 error test.
        Create route to abort the request with the 500 Error.
        Returns:
        """

        @self.app.route('/500')
        def internal_server_error():
            abort(500)

        response = self.client.get('/500')
        self.assertEqual(response.status_code, 500)
        self.assertTrue("500 Error".encode() in response.data)
        logger.info(f"Access is denied,server error, status: {response.status_code}. Test is done")


if __name__ == '__main__':
    unittest.main()