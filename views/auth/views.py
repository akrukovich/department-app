# 3rd party imports
from flask import flash, redirect, render_template, url_for, request
from flask_login import login_required, login_user, logout_user
from views.auth.forms import LoginForm, RegistrationForm
from app import db
from models.models import Employee
from loggers import get_logger
from . import auth


logger = get_logger(__name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    form = RegistrationForm()

    if form.validate_on_submit():
        employee = Employee(username=form.username.data,
                            email=form.email.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            date_of_birth=form.date_of_birth.data,
                            password=form.password.data
                            )

        # add employee to the database
        db.session.add(employee)
        db.session.commit()
        logger.info(f'{employee.email} {employee.username} has registered')

        flash('You have successfully registered! You may log in now.', 'success')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm(request.form)

    if form.validate_on_submit():

        # check whether employee exists in database and whether
        # the password entered matches the password in the database
        employee = Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(form.password.data):

            # log employee in
            login_user(employee)
            logger.info(f'{employee.email} {employee.username} admin:{employee.is_admin} logged in')

            # redirect to the appropriate dashboard page
            if employee.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            return redirect(url_for('home.dashboard'))

        # when login details are incorrect
        else:
            logger.info(f'{employee.email} {employee.username} '
                        f'admin:{employee.is_admin} entered invalid data')
            flash('Invalid email or password')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))
