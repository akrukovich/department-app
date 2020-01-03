# 3rd party imports
from flask import Blueprint

# Local import
admin = Blueprint('admin', __name__)
import app.admin.views as views

