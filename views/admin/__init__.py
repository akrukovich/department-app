# 3rd party imports
from flask import Blueprint


admin = Blueprint('admin', __name__)
import views.admin.views as views
