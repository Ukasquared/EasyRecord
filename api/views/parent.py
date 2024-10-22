#!/usr/bin/python3
"""parent view function"""
from ..views import app_routes
from api.views.role import role_required
from flask import request, jsonify
from api.models import storage
from api.models.parent import Parent
from api.models.student import Student
# from models.course import Course


@role_required('parent')
@app_routes.route('/parent_dashboard', strict_slashes=False)
def parent_dashboard():
    """returns student
    scores"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "missing or invalid json file"}), 400
    email = data.get('email')
    if email:
        parent = storage.find_user(Parent, email=email)
        # fetch the parents information
        # fetch the student names, course offered and score that is connected to the parent
        # student_id = parent.student_id
        # student = storage.find_user(Student, id=student_id)
        student = parent.student
        course_detail = []
        if student:
            for course in student.course:
                d_course = {}
                d_course[course.title] = course.score
                course_detail.append(d_course)

        parent_data = {"parent": {
            'id':  parent.id,
            'firstname': parent.firstname,
            'lastname': parent.lastname,
            "email": parent.email,
            "gender": parent.gender,
            "photo": parent.photo
        }, "student": {
            "student_id": student.id,
            'firstname': student.firstname,
            'lastname': student.lastname,
            "course": course_detail
        }}
        return jsonify(parent_data), 200
    return jsonify({"error": "missing or invalid json file"}), 400