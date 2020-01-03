# 3rd party imports
from flask import Blueprint

# Local import
auth = Blueprint('auth', __name__)
import app.auth.views as views

