from ..views import app_routes
from flask import request, send_from_directory
from werkzeug.utils import secure_filename
from api.auth import Auth
from flask import abort, jsonify, redirect, make_response
from flask_jwt_extended import create_access_token
from datetime import timedelta
import os

auth = Auth()

uploads = 'images'

ALLOWED_EXTENSIONS = {'jpeg', 'jpg', 'png'}
os.makedirs(uploads, exist_ok=True)


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    

@app_routes.route('/', methods=["GET"], strict_slashes=False)
def hello_world():
    return jsonify({"msg": "it is working"})



@app_routes.route('/login', methods=['POST'], strict_slashes=False)
def login_user():
    """log a user in"""
    
    if request.method == "POST":
        data = request.get_json()
        if data:
            # role = data.get('role')
            email = data.get('email')
            password = data.get('password')
            role = auth.get_user_role_id(email)
            if email and password and role:
                state = auth.validate_login(email, password)               
            if state:
                session_id = auth.create_session(email)
                print(session_id)
                # create a jwt token with the users role included
                access_token = create_access_token(identity=role, additional_claims={'email': email}, expires_delta=(timedelta(minutes=30)))
                response_body = jsonify({'token': access_token, 'role': role})
                response = make_response(response_body, 200)
                response.set_cookie("session_id", session_id, httponly=True)
                return response
        abort(405)
    

@app_routes.route('/logout', methods=['DELETE'], strict_slashes=False)
def logout_user():
    """ logout a user by 
    destroying the
    session """
    cookie = request.cookies.get('session_id')
    user = auth.get_usr_from_session_id(cookie)
    if user:
        auth.destroy_session(user.id)
        return jsonify({"message": "user exist"})
        # redirect('/')
    else:
        abort(403)


@app_routes.route('/reset_password', methods=['POST, PUT'], strict_slashes=False)
def reset_password():
    """reset 
    password"""
    if request.method == 'POST':
        email = request.form['email']
        try:
            token = Auth.reset_password_token(email)
            return jsonify({"email": email, 
                            "reset_token": token}), 200
        except:
            abort(403)
    elif request.method == "PUT":
        try:
            token = request.form['reset_token']
            password = request.form['new_password']
            Auth.update_password(token, password)
        except:
            abort(403)


# send and save file in the file system
# this should hand also sign up
@app_routes.route('/signup', methods=['POST'], strict_slashes=False)
def sign_up():
    """uploads, 
    a picture to 
    dashboard"""
    if request.method == 'POST':
        form_data = dict(request.form)
        if 'photo' not in request.files:
            abort(400)
        file = request.files.get('photo')
        if file.filename == '':
            abort(400)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(uploads, filename))
        form_data['photo'] = filename
        try:
            obj_id = auth.register_user(**form_data)
        except ValueError:
            abort(400)
        print(obj_id)
        return jsonify({'message': obj_id}), 200

# route to serve file
@app_routes.route(f"/{uploads}/<path:filename>", methods=["GET"])
def serve_file(filename):
    """serve file"""
    abs_path = os.path.abspath(uploads)
    print(f"Serving from: {abs_path}")
    return send_from_directory(abs_path, filename)