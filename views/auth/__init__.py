# 3rd party imports
from flask import Blueprint

# Local import
auth = Blueprint('auth', __name__)

import views.auth.views as views
