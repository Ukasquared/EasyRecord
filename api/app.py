#!/usr/bin/python3
"""routes"""
from flask import Flask, jsonify
from flask_cors import CORS
from views import app_routes
from flask_jwt_extended import JWTManager

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'gQWwyO14gh5HGOdcvQPL56ODG43OND32APB@2#2&46'
jwt = JWTManager(app)

app.register_blueprint(app_routes)


@app.errorhandler(404)
def not_found() -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def not_authorized() -> str:
    """ not_authorized
    """
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(400)
def invalid_json() -> str:
    """ invalid json
    """
    return jsonify({"error": "missing or invalid json file"}), 400


@app.errorhandler(403)
def not_allowed() -> str:
    """ not allowed
    handler
    """
    return jsonify({"error": "Forbidden"}), 403

@app.errorhandler(407)
def first_authenticate() -> str:
    """ not allowed
    handler
    """
    return jsonify({"error": "incorrect credentials"}), 407

# @app.before_request
# def authorization():
#    """allow only authorized
#   access """
#    request_path = ['login', 'signup']
# 
 

if __name__ == '__main__':
    app.run("0.0.0.0", "5000", debug=True)