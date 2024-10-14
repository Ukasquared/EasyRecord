#!/usr/bin/python3
from views import app_routes, role_required
from flask import request, abort, jsonify
from models.student import Student
from models.admin import Admin
from models.course import Course
from api.auth import Auth
from models import storage

# enroll student in course - endpoint
# assign admin for a course - endpoint

upload_folder = '/api/files/'

@role_required('admin')
@app_routes.route('/enroll_student_in_course', methods=["POST"], strict_slashes=False)
def enroll_student():
    """enroll student into
    a course"""
    # request should contain student id and course id
    # we need the to fetch the student using their id, then the course using the course id
    # then we append the course to the student.courses
    # check if user has already been enrolled

    if request.method == "POST":
        data = request.get_json()
        if not data:
            abort(400)
        student_id = data.get("student_id")
        course_id = data.get("course_id")
        if not student_id or not course_id:
            abort(400)
        try:
            student_name = Auth.enroll_student_course(course_id, student_id)
            return jsonify({"msg": f"{student_name} successfully registered"})
        except ValueError:
            abort(400)


@role_required('admin')
@app_routes.route('/admin_dashboard', methods=['POST'], strict_slashes=False)
def admin_dashboard():
    """fetch admin personal information,
    total number of teachers, and
    total number of student"""
    # # all courses title and their id (list of list)
    # request should contain admin id and course id
    if request.method == "POST":
        data = request.get_json()
        if not data:
            abort(407)
        email = data.get("email")
        if email:
            admin = storage.find_user(Admin, email=email)
            if not admin:
                abort(407)
            total_student = len(admin.students)
            total_teacher = len(admin.teachers)
            all_courses = []
            for course in admin.courses:
                courses_list = [course.id, course.title]
                all_courses.append(courses_list)
            
            admin_data = {
                        'id':  admin.id,
                        'firstname': admin.firstname,
                        'lastname': admin.lastname,
                        "email": admin.email,
                        "gender": admin.gender,
                        "photo": f"{upload_folder}{admin.photo}",
                        "courses_with_id": all_courses,
                        "total_student": total_student,
                        "total_ teacher": total_teacher
                    }
            return jsonify(admin_data), 200