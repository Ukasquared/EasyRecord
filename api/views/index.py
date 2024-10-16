from ..views import app_routes
from flask import request, send_from_directory
from werkzeug.utils import secure_filename
from api.auth import Auth
from flask import abort, jsonify, redirect
from flask_jwt_extended import create_access_token
from datetime import timedelta
import os



upload_folder = '/api/files/'
ALLOWED_EXTENSIONS = {'jpeg', 'jpg', 'png'}


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    

@app_routes.route('/login', methods=['POST'], strict_slashes=False)
def login_user():
    """log a user in"""
    email = request.form['email']
    role =  request.form['role']
    password = request.form['password']

    if email and password and role:
        state = Auth.validate_login(email, password, role)
        if not state:
            abort(407)
        session_id = Auth.create_session(email, role)
        # create a jwt token with the users role included
        access_token = create_access_token(identity={'role': role}, expires_delta=(timedelta(minutes=30)))
        response = jsonify(access_token=access_token)
        response.set_cookie("session_id", session_id)
        return response, 200


@app_routes.route('/logout', methods=['DELETE'], strict_slashes=False)
def logout_user():
    """ logout a user by 
    destroying the
    session """
    cookie = request.cookies.get('session_id')
    user = Auth.get_usr_from_session_id(cookie)
    if user:
        Auth.destroy_session(user.id)
        redirect("/")
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
@app_routes.route('/sign_up', methods=['POST'], strict_slashes=False)
def sign_up():
    """uploads, 
    a picture to 
    dashboard"""
    if request.method == 'POST':
        form_data = dict(request.form)
        if 'photo' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400
        file = request.files.get('photo')
        if file.filename == '':
            return jsonify({"error": "no file was uploaded"}), 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_folder, filename))
        form_data['photo'] = filename
        obj_id = Auth.register_user(form_data)
        return jsonify({'message': obj_id}), 200
    abort(403)


# route to serve file
@app_routes.route(f"{upload_folder}<path:filename>", methods=["GET"])
def serve_file(filename):
    """serve file"""
    return send_from_directory(upload_folder, filename)