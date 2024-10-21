"""routes"""

from flask import Flask, jsonify
from flask_cors import CORS
from .views import app_routes
from flask_jwt_extended import JWTManager


app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'gQWwyO14gh5HGOdcvQPL56ODG43OND32APB@2#2&46'
# app.config['UPLOADS'] = 'images'
jwt = JWTManager(app)


app.register_blueprint(app_routes)


@jwt.expired_token_loader
def expired_token_handler(jwt_header, jwt_payload):
    return jsonify({'msg': 
                    'the token has expired'}), 401


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def not_authorized(error) -> str:
    """ not_authorized
    """
    return jsonify({"error": "Unauthorized Access"}), 401

@app.errorhandler(400)
def invalid_json(error) -> str:
    """ invalid json
    """
    return jsonify({"error": "missing or invalid json file"}), 400


@app.errorhandler(403)
def not_allowed(error) -> str:
    """ not allowed
    handler
    """
    return jsonify({"error": "Forbidden"}), 403

@app.errorhandler(405)
def first_authenticate(error) -> str:
    """ not allowed
    handler
    """
    return jsonify({"error": "incorrect credentials"}), 405

@app.errorhandler(500)
def server_error(error) -> str:
    """ not allowed
    handler
    """
    return jsonify({"error": "server error"}), 500

# @app.before_request
# def authorization():
#    """allow only authorized
#   access """
#    request_path = ['login', 'signup']
# 
 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
