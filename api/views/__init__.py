from flask import Blueprint


app_routes = Blueprint('app_routes', __name__, url_prefix='/api')

from ..views.index import *
from ..views.admin import *
from ..views.teacher import *
from ..views.parent import *
from ..views.course import *



