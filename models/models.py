# third-party imports
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# local imports
from app import db, login_manager


class Employee(UserMixin, db.Model):
    """Create an Employee model

    Objects of this class suit to employees' data
    and admin info contains here.
    """

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    department_name = db.Column(db.String(60), db.ForeignKey('departments.name'))
    date_of_birth = db.Column(db.DATE)
    salary = db.Column(db.DECIMAL, index=True)
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """Prevent password from being accessed.

        Prevent password from being accessed by raising attribute error.

        Raises:
            AttributeError: password is not a readable attribute

        """

        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """Set password to a hashed password

        Set user's password to the hashed form
        Args:
            password: User's password of str data type

        Returns:
            None

        """

        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """Check if hashed password matches actual password

        Verifying of password and hashed value matching
        Args:
            password:the plaintext password to compare against the hash

        Returns: Return `True` if the password matched, `False` otherwise.

        """

        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        """
        Employee representation

        Magic function that represent Employee status
        Returns: Str form of Employee

        """
        return f'<Employee: {self.username}>'


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    """Return user by id

    Return user id for view presentation
    Args:
        user_id: Employee's id

    Returns: employee object of certain id

    """
    return Employee.query.get(int(user_id))


class Department(db.Model):
    """Create a Department object

    """

    __tablename__ = 'departments'

    department_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)

    def __repr__(self):
        """
        Department representation

        Magic function that represent Department status
        Returns: 'Str' form of Department

        """
        return f'Department: {self.name}'

    def __str__(self):
        """Department representation for client

        Magic function that show Department name for client
        Returns: Department name

        """
        return f'{self.name}'
