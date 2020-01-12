# Third-party imports
import unittest
from datetime import datetime

from tests.util import TestBase

# Local imports
from models.models import Employee, Department
from loggers import get_logger

logger = get_logger(__name__)


class TestModels(TestBase):

    def test_employee_model(self):
        """
        Test number of records in Employee table.
        """

        self.assertEqual(Employee.query.count(), 2)
        employee = Employee.query.get(2)
        self.assertEqual(employee.email, 'test@test.com')
        self.assertEqual(employee.salary, 1000)
        date = datetime.strptime('1996-01-01', '%Y-%m-%d').date()
        self.assertEqual(employee.date_of_birth, date)

        with self.assertRaises(AttributeError):
            Employee.query.first().password

    def test_department_model(self):
        """
        Test number of records in Department table
        """

        # create test department
        department = Department.query.first()

        # save department to database
        logger.info(f'Department {department.name} has been tested')

        self.assertEqual(Department.query.count(), 1)
        self.assertEqual(department.__str__(), 'TestDep')


if __name__ == '__main__':
    unittest.main()