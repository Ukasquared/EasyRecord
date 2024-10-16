#!/usr/bin/python3
"""parent view function"""
from ..views import app_routes, role_required
from flask import request, abort, jsonify
from api.models import storage
from api.models.parent import Parent
from api.models.student import Student
# from models.course import Course


upload_folder = '/api/files/'

@role_required('parent')
@app_routes.route('/parent_dashboard', strict_slashes=False)
def parent_dashboard():
    """returns student
    scores"""
    data = request.get_json()
    if not data:
        abort(407)
    email = data.get('email')
    if email:
        parent = storage.find_user(Parent, email=email)
        # fetch the parents information
        # fetch the student names, course offered and score that is connected to the parent
        student_id = parent.student_id
        student = storage.find_user(Student, id=student_id)
        course_detail = []
        if student:
            for course in student.course:
                d_course = {}
                d_course[course.title] = course.score
                course_detail.append(d_course)

        user_data = {"parent": {
            'id':  parent.id,
            'firstname': parent.firstname,
            'lastname': parent.lastname,
            "email": parent.email,
            "gender": parent.gender,
            "photo": f"{upload_folder}{parent.photo}"
        }, "student": {
            "student_id": student_id,
            'firstname': student.firstname,
            'lastname': student.lastname,
            "course": course_detail
        }}

        return jsonify(user_data), 200

