# Third-party imports
from flask import url_for
from flask_login import login_user, current_user, logout_user
from app.models import Employee
from loggers import get_logger
from app.util import TestBase
import unittest
from flask import url_for
from flask_login import login_user, current_user, logout_user
from models.models import Employee
from loggers import get_logger
from tests.util import TestBase

# Local imports

logger = get_logger(__name__)




class TestHomeViews(TestBase):
    """Class for home views testing.

    """

    def test_homepage_view(self):
        """Test that homepage is accessible without login.

         Test homepage accessing and correct template rendering/
        Returns:
            None
        """
        response = self.client.get(url_for('home.homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('home/index.html')
        logger.info(f'Homepage status: {response.status_code}. Test is done.')

    def test_dashboard_view(self):
        """Dashboard testing.

        Test that dashboard is inaccessible without login
        and redirects to login page then to dashboard.
        Returns:
            None

        """
        target_url = url_for('home.dashboard')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        logger.info(f'No access to home.dashboard, status: {response.status_code}')
        self.assertRedirects(response, redirect_url)
        logger.info(f'Redirected to login page  status: {response.status_code}. Test is done')

    def test_admin_dashboard_view(self):
        """Admin dashboard testing.

        Test that dashboard is inaccessible without login
        and redirects to login page then to dashboard
        Returns:
            None

        """
        target_url = url_for('home.admin_dashboard')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        logger.info(f'No access to home.admin.dashboard, status: {response.status_code}')
        self.assertRedirects(response, redirect_url)
        logger.info(f'Redirected to login page  status: {response.status_code}. Test is done')


class TestAuthViews(TestBase):
    """Class for auth views testing.

    """

    def test_register_view(self):
        """Registration view test.

        Test response from registration view and correct template.
        Returns:
            None

        """
        response = self.client.get(url_for('auth.register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('auth/register.html')
        logger.info(f'register page status: {response.status_code}. Test is done.')

    def test_login_view(self):
        """Test that login page is accessible without login.

        Test response from login view and correct template.
        Returns:
            None

        """

        response = self.client.get(url_for('auth.login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('auth/login.html')
        logger.info(f'Login page status: {response.status_code}. Test is done.')

    def test_logout_view(self):
        """Logout test.

        Test that logout link is inaccessible without login
        and redirects to login page then to logout.
        Returns:
            None

        """
        target_url = url_for('auth.logout')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        logger.info(f'No access to logout before logging in, status: {response.status_code}')
        self.assertRedirects(response, redirect_url)
        logger.info(f'Redirected to login page  status: {response.status_code}. Test is done')


class TestAdminViews(TestBase):
    """Class for admin views testing.

    """
    def test_check_admin(self):
        """Test check_admin.

        Test is current user is admin.
        Returns:
            None

        """
        employee = Employee.query.filter_by(username='test_user').first()
        login_user(employee)
        self.assertEqual(current_user.is_admin, False)
        logout_user()
        admin = Employee.query.filter_by(username='admin').first()
        login_user(admin)
        self.assertEqual(current_user.is_admin, True)


if __name__ == '__main__':
    unittest.main()
