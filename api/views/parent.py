#!/usr/bin/python3
"""parent view function"""
from views import app_routes, role_required
from flask import request, abort
from models import storage
from models.parent import Parent 


upload_folder = '/api/files/'

@role_required('parent')
@app_routes.route('/parent_dashboard', strict_slashes=False)
def parent_dashboard():
    """returns student
    scores"""
    data = request.get_json()
    if not data:
        abort()
    email = data.get('email')
    user = storage.find_user(Parent, email=email)
    # fetch the parents information
    # fetch the student names, course offered and
    # score that is connected to the parent
    user_data = {
        'id':  user.id,
        'lastname': user.lastname,
        "email": user.email,
        "gender": user.gender,
        "photo": f"{upload_folder}{user.photo}",
        "role": user.role,
        "student_id": user.student_id,
        "student_name":,
        "course_score":,
    }

