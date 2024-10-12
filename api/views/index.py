from views import app_routes
from flask import request
from api.auth import Auth
from flask import abort, jsonify, redirect


@app_routes.route('/login', methods=['POST'])
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
        response = jsonify('login succesful')
        response.set_cookie("session_id", session_id)
        return response, 200

@app_routes.route('/logout', methods=['DELETE'])
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

app_routes.route('/reset_password', methods=['POST, PUT'])
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