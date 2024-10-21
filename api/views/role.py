"""role required class"""
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify
from functools import wraps

def role_required(user_role):
    """a decorator function"""
    def wrapper(fn):
        @jwt_required()
        @wraps(fn)
        def invoked_func(*args, **kwargs):
            claim = get_jwt_identity()
            if claim != user_role:
                return jsonify({"msg": "Unauthorized access"}), 401
            return fn(*args, **kwargs)
        return invoked_func
    return wrapper