# Third-party imports
import unittest
from datetime import datetime

# Local imports
from views.admin.forms import DepartmentForm, EmployeeEditForm, department_query, get_pk
from views.auth.forms import RegistrationForm, LoginForm
from models.models import Department
from loggers import get_logger
from tests.util import TestBase

logger = get_logger(__name__)


class TestAuthForms(TestBase):

    def test_validate_success_register_form(self):
        """Test whether registration works correctly.

        Returns:
            None

        """

        date = datetime.strptime('1996-01-01', '%Y-%m-%d').date()
        form = RegistrationForm(
            email='test@gmail.com',
            username='test',
            first_name='test',
            last_name='test',
            date_of_birth=date,
            password='example',
            confirm_password='example',
            csrf_enabled=False

        )
        self.assertTrue(form.validate())

    def test_validate_invalid_password_format(self):
        """Test incorrect data does not validate.

        Returns:
            None
        """

        date = datetime.strptime('1996-01-01', '%Y-%m-%d').date()
        form = RegistrationForm(
            email='test@gmail.com',
            username='test',
            first_name='test',
            last_name='test',
            date_of_birth=date,
            password='example',
            confirm_password='1111',
            csrf_enabled=False
        )
        self.assertFalse(form.validate())

    def test_validate_email_already_registered(self):
        """Test user can't register when a duplicate email is used.

        Returns:
            None

        """

        date = datetime.strptime('1996-01-01', '%Y-%m-%d').date()
        form = RegistrationForm(
            email='test@test.com',
            username='test',
            first_name='test',
            last_name='test',
            date_of_birth=date,
            password='example',
            confirm_password='example',
            csrf_enabled=False
        )
        self.assertFalse(form.validate())

    def test_validate_success_login_form(self):
        # Ensure correct data validates.
        form = LoginForm(email='test@user.com', password='just_a_test_user', csrf_enabled=False)
        self.assertTrue(form.validate())

    def test_validate_invalid_email_format(self):
        # Ensure invalid email format throws error.
        form = LoginForm(email='unknown', password='example', csrf_enabled=False)
        self.assertFalse(form.validate())


class TestAdminForms(TestBase):

    def test_validate_success_department_form(self):
        form = DepartmentForm(name='Test', csrf_enabled=False)
        self.assertTrue(form.validate())

    def test_department_query(self):
        query = department_query().count()
        self.assertEqual(query, 1)

    def test_get_pk(self):
        for i in Department.query.all():
            print(i, 'asssasdasdasd')
        department = department_query().first()
        department = get_pk(department)
        self.assertEqual(department, 'TestDep')

    def test_validate_success_employee_form(self):
        department = Department.query.first()
        date = datetime.strptime('1996-01-01', '%Y-%m-%d').date()
        form = EmployeeEditForm(
            department_name=department,
            first_name='Test',
            last_name='Test',
            date_of_birth=date,
            salary=1000,
            csrf_enabled=False
        )
        self.assertTrue(form.validate())


if __name__ == '__main__':
    unittest.main()
