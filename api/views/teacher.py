#!/usr/bin/python3
from flask import request, abort, jsonify
from api.views import app_routes
from api.views.role import role_required
from api.models import storage
from api.models.teacher import Teacher
from api.models.course import Course
from api.models.student import Student
# fetch the teachers details from the database
# fetch the courses they teach
# fetch the names of student offering their course


@app_routes.route('/teachers_dashboard', methods=['POST'], strict_slashes=False)
@role_required('teacher')
def teachers_dashboard():
    if request.method == "POST":
        data = request.get_json()
        if data:
            email = data.get('email')
            if email:
                teacher = storage.find_user(Teacher, email=email)
                if teacher:
                    if teacher.student:
                        student_list = []
                        for student in teacher.student:
                            student_names = [student.firstname, student.lastname]
                            student_list.append(student_names)
                    teacher_data = {"teacher": {
                        'id':  teacher.id,
                        'firstname': teacher.firstname,
                        'lastname': teacher.lastname,
                        "email": teacher.email,
                        "gender": teacher.gender,
                        "photo": teacher.photo,
                        "course": teacher.course.title,
                    }, "students": student_list 
                    }
                    return jsonify(teacher_data), 200
        return jsonify({"error": "missing or invalid json file"}), 400


@app_routes.route('/search_for_student', methods=['POST'], strict_slashes=False)
@role_required('teacher')
def search_for_student_by_name():
    """search for student
    """
    if request.method == "POST":
        data = request.get_json()
        if not data:
            return jsonify({"error": "Forbidden"}), 403
        student_name = data.get('name')
        if not student_name:
            return jsonify({"error": "Forbidden"}), 403
        student = storage.find_user(Student, first_name=student_name)
        return jsonify({
            'id':  student.id,
            'firstname': student.firstname,
            'lastname': student.lastname,
            "gender": student.gender
        })


@app_routes.route('/grade_student', methods=['POST'], strict_slashes=False)
@role_required('teacher')
def grade_student():
    """grading students
       - the id of student,
         their score, course title
         will be used to record
         the student score
    """
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Forbidden"}), 403
        score = data.get('score')
        student_id = data.get('id')
        course_title = data.get('title')
        if not score or not student_id or not course_title:
            return jsonify({"error": "Forbidden"}), 403
        student = storage.find_user(Student, id=student_id )
        course = storage.find_user(Course, title=course_title, student=student)
        course.score = int(score)
        storage.save()
        return jsonify({"message": "student successfully graded"}), 200
        
