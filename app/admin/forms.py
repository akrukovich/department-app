# 3rd party imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Optional
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField
# Local imports
from app.models import Department


class DepartmentForm(FlaskForm):
    """Form for admin to add or edit a department.

    """
    name = StringField('Name', validators=[DataRequired()])
    # desciption = StringField('Description',validators=[DataRequired]) # ToDO make that on Future
    submit = SubmitField('Submit')


def department_query():
    """Query for Employee editing form.

    Returns:
         Department.query: query of names of Departments

    """

    return Department.query


def get_pk(obj):
    """Function which can be passed as a get_pk parameter

    Args:
        obj:

    Returns:
        obj: Str form of object

    """

    return str(obj)


class EmployeeEditForm(FlaskForm):
    """Form for admin to assign and edit employees
    """
    department_name = QuerySelectField(query_factory=department_query, get_label='name', label='Department',
                                       get_pk=get_pk)
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    date_of_birth = DateField('Date of birth', validators=[Optional()], format='%Y-%m-%d')
    salary = DecimalField('Salary', validators=[DataRequired()])

    submit = SubmitField('Submit')
