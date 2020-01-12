# third-party imports
from flask import render_template, abort
from flask_login import login_required, current_user
# local imports
from views.home import home


@home.route('/')
def homepage():
    """Render the homepage template on the / route.
    Render homepage, otherwise raise errors.
    Returns:
         home/index.html: homepage html.

    """
    return render_template('home/index.html')


@home.route('/dashboard')
@login_required
def dashboard():
    """Render the dashboard template on the /dashboard route.

    Render dashboard, otherwise raise errors.
    Returns:
        home/dashboard.html: dashboard html.

    """
    return render_template('home/dashboard.html', title="Dashboard")


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    """Return rendered admin-user page.

    Render admin-user page after checking out admin rights.
    Returns:
        home/admin_dashboard.html: admin dashboard html
    """

    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title='Dashboard')
