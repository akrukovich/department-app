# 3rd party imports
from flask import Blueprint


home = Blueprint('home', __name__)

# Local import
import views.home.views as views
