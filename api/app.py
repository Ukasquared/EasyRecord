#!/usr/bin/python3
"""routes"""
from flask import Flask, jsonify
from flask_cors import CORS
from views import app_routes

app = Flask(__name__)
CORS(app)

app_routes.register_blueprint(app_routes)


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


if __name__ == '__main__':
    app.run("0.0.0.0", "5000")