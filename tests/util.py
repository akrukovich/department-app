# Third-party imports
from datetime import datetime
from flask_testing import TestCase
from models.models import Employee, Department
from loggers import get_logger
from app import create_app, db


logger = get_logger(__name__)


class TestBase(TestCase):

    def create_app(self):
        """ Create Flask application and connect to the test database for testing.
        Create for model testing flask application object and connect to the test database.
        Returns:
             app: Flask object
        """
        # Pass in test configurations
        config_name = 'testing'
        app = create_app(config_name)


        # app.config.update(SQLALCHEMY_DATABASE_URI='mysql://root:Ak12345678@localhost/dep_db_test') # Local
        app.config.update(SQLALCHEMY_DATABASE_URI='mysql://root:@127.0.0.1/dep_db_test') #travis-si

        return app

    def setUp(self):
        """Create tables and fill them up with testing data.
        Being invoked before each test of current class for creating test tables and filling them.
        Returns:
            None
        """
        db.create_all()
        logger.info('Test database has been created')

        # Create test admin user.
        admin = Employee(email='admin@admin.com', username='admin', password='admin', is_admin=True)
        logger.info(f'{admin.username} has been created')

        # Create test non-admin user.
        employee = Employee(email='test@test.com',
                            first_name='Test',
                            last_name='TestLastName',
                            username="test_user",
                            salary=1000,
                            date_of_birth=datetime.strptime('1996-01-01', '%Y-%m-%d').date(),
                            password="test"

                            )
        logger.info(f'{employee.username} has been created')

        # Create test department.
        department = Department(name='TestDep')
        logger.info(f'{department.name} has been created')

        # save users to database
        db.session.add(department)
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()
        logger.info(f'Test {department.name}, {admin.username} '
                    f'and {employee.username} have been committed')


    def tearDown(self):
        """Delete tables and testing data.
        Being invoked after each test of current class for deleting test tables and data.
        Returns:
            None
        """
        db.session.remove()
        db.drop_all()
        logger.info('''Test database has been deleted
--------------------------------------------------------------------------------------'''
                    )