# 3rd party imports
from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from sqlalchemy import exc
from sqlalchemy import func
# Local imports
from views.admin import admin
from views.admin.forms import DepartmentForm, EmployeeEditForm
from app import db
from models.models import Department, Employee
from loggers import get_logger


logger = get_logger(__name__)


def check_admin():
    """Prevent non-admins from accessing the page

     Return:
         403 error

    """
    if not current_user.is_admin:
        abort(403)


@admin.route('departments', methods=['Get'])
@login_required
def list_departments():
    """
    List of all departments

    return a rendered template of departments
    """
    check_admin()
    avg_info = dict()

    avg_data = Employee.query.with_entities(
        Employee.department_name,
        func.avg(Employee.salary).label('salary')
    ).group_by(Employee.department_name)

    for unit in avg_data:
        if unit.department_name:
            avg_info[unit.department_name] = unit.salary

    departments = Department.query.all()

    return render_template('admin/departments/departments.html',
                           departments=departments, title='Departments', avg_info=avg_info)


@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Add a department to the database
    """
    #  Throws a 403 Forbidden error if a non-admin user attempts to access these views.
    check_admin()

    add_department = True

    form = DepartmentForm()
    if form.validate_on_submit():

        department = Department(name=form.name.data)

        try:
            # add a department to the database
            db.session.add(department)
            db.session.commit()

            logger.info(f'Department {department.name} has been added')

            flash('The new department have been successfully added !')
        except exc.IntegrityError:
            logger.exception('Add department exc.IntegrityError')
            flash('Error: department name already exists.')

        return redirect(url_for('admin.list_departments'))

    return render_template('admin/departments/department.html', action='Add',
                           add_department=add_department,
                           form=form,
                           title='Add Department')


@admin.route('/department/edit/<int:department_id>', methods=['POST', 'GET'])
@login_required
def edit_department(department_id):
    '''
    Edit a department

    '''

    #  Throws a 403 Forbidden error if a non-admin user attempts to access these views.
    check_admin()

    add_department = False

    department = Department.query.get_or_404(department_id)
    logger.info(f'Id: {department.department_id} Department edited from {department.name}')
    form = DepartmentForm(obj=department)

    if form.validate_on_submit():
        department.name = form.name.data
        db.session.commit()
        logger.info(f'Id: {department.department_id} Department edited to {department.name}')
        flash('You have successfully edited the department.')

        return redirect(url_for('admin.list_departments'))

    form.name.data = department.name

    return render_template('admin/departments/department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Department")


@admin.route('/departments/delete/<int:department_id>', methods=['GET', 'POST'])
@login_required
def delete_department(department_id):
    """
    Delete a department from the database

    """
    #  Throws a 403 Forbidden error if a non-admin user attempts to access these views.
    check_admin()

    try:
        department = Department.query.get_or_404(department_id)
        db.session.delete(department)
        logger.warning(f'Department {department.name} is ready to be deleted -')
        db.session.commit()
        logger.info(f'Department {department.name} has been deleted -')

        flash('The department have been successfully deleted !')

    except exc.IntegrityError as e:
        logger.exception('MySQLdb._exceptions.IntegrityError')
        flash('Departments cannot be deleted with employees! We are not Ciklum !!!')
        return redirect(url_for('admin.list_departments'))

    # redirect to the departments page
    return redirect(url_for('admin.list_departments'))


@admin.route('/employees')
@login_required
def list_employees():
    """
    List all employees
    """
    check_admin()

    # employees = Employee.query.order_by(Employee.first_name, Employee.last_name).all()
    employees = Employee.query.all()

    return render_template('admin/employees/employees.html',
                           employees=employees, title='Employees')


@admin.route('/employees/add', methods=['GET', 'POST'])
@login_required
def add_employee():
    """
    Add an employee to the database
    """
    #  Throws a 403 Forbidden error if a non-admin user attempts to access these views.
    check_admin()

    add_employee = True

    form = EmployeeEditForm()

    if form.validate_on_submit():
        employee = Employee(department_name=form.department_name.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            date_of_birth=form.date_of_birth.data,
                            salary=form.salary.data
                            )

        db.session.add(employee)
        db.session.commit()
        logger.info(f'Add employee Id: {employee.id}, first name: {employee.first_name},'
                    f'last name: {employee.last_name} has been added. ')

        flash(f'{employee.first_name} {employee.last_name}  have been successfully added !')

        return redirect(url_for('admin.list_employees'))

    return render_template('admin/employees/employee.html', action='Add',
                           add_employee=add_employee,
                           form=form,
                           title='Add Employee'
                           )


@admin.route('/employees/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_employee(id):
    """
     Assign a department to an employee
    """
    check_admin()

    employee = Employee.query.get_or_404(id)
    logger.info(f'Edit employee Id: {employee.id} {employee.first_name} {employee.last_name}')
    # prevent admin from being assigned a department
    if employee.is_admin:
        abort(403)

    form = EmployeeEditForm(obj=employee)

    if form.validate_on_submit():
        employee.department_name = form.department_name.data
        employee.first_name = form.first_name.data
        employee.last_name = form.last_name.data
        employee.date_of_birth = form.date_of_birth.data
        employee.salary = form.salary.data

        db.session.add(employee)
        db.session.commit()
        logger.info(f'Id: {employee.id}, first name: {employee.first_name},'
                    f'last name: {employee.last_name} has been edit. ')

        flash('The employee has been succesfully edit !')

        # redirect to the employees page
        return redirect(url_for('admin.list_employees'))

    return render_template('admin/employees/employee.html',
                           employee=employee, form=form,
                           title='Edit Employee')


@admin.route('/employees/delete/<int:id>', methods=['POST', 'GET'])
@login_required
def delete_employee(id):
    """
    Delete a department from the database

    """
    #  Throws a 403 Forbidden error if a non-admin user attempts to access these views.
    check_admin()

    employee = Employee.query.get_or_404(id)
    logger.info(f'Delete employee Id: {employee.id} first name: {employee.first_name}'
                f' last name: {employee.last_name}')
    db.session.delete(employee)
    db.session.commit()
    logger.info(f'Id: {employee.id}, first name: {employee.first_name},'
                f'last name: {employee.last_name} has been deleted. ')

    flash(f'{employee.first_name} {employee.last_name} has been fired or gone!')

    # redirect to the departments page
    return redirect(url_for('admin.list_employees'))
