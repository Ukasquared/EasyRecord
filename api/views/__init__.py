from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt
from views.index import *

app_routes = Blueprint('app_routes', __name__)


def role_required(user_role):
    """a decorator function"""
    def wrapper(fn):
        @jwt_required()
        def invoked_func(args, kwargs):
            claims = get_jwt()
            if claims['role'] != user_role:
                abort(401)
            return fn(args, kwargs)
        return invoked_func
    return wrapper