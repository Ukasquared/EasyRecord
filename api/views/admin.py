#!/usr/bin/python3
from views import app_routes, role_required

# enroll student in course - endpoint
# assign teacher for a course - endpoint



@role_required('admin')
@app_routes.route('/enroll_student_in_course', strict_slashes=False)
def enroll_student():
    """enroll student into
    a course"""
    # request should contain student id and course id


@role_required('admin')
@app_routes.route('/enroll_teacher_in_a_course', strict_slashes=False)
def enroll_teacher():
    """enroll teacher into
    a course"""
    # request should contain teacher id and course id


@role_required('admin')
@app_routes.route('/admin_dashboard', strict_slashes=False)
def admin_dashboard():
    """fetch admin personal information,
    total number of teachers, and
    total number of student"""
    # # all courses title and their id
    # request should contain teacher id and course id
