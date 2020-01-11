from tests.util import TestBase


class TestFactory(TestBase):
    '''Testing factory method.

    '''
    def test_config(self):
        """Test configuration of the application.

        Returns:
            None

        """
        self.assertTrue(self.app.testing)
