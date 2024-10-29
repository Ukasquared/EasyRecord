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


@app_routes.route('/teachers_dashboard', methods=['GET'], strict_slashes=False)
@role_required('teacher')
def teachers_dashboard():
    if request.method == "GET":
        session_id = request.cookies.get('session_id')
        if session_id:
            teacher = storage.find_user(Teacher, session_id=session_id)
            if teacher:
                print(teacher)
                student_list = []
                if teacher.student:
                    for student in teacher.student:
                        student_names = [student.firstname, student.lastname]
                        student_list.append(student_names)
                teacher_data = {"teacher": {
                    "photo": teacher.photo,
                    "gender": teacher.gender,
                    "course": teacher.course.title,
                    'id':  teacher.id,
                    'name': f"{teacher.firstname} {teacher.lastname}",
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
        student = storage.find_user(Student, firstname=student_name)
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
        if not student or not student.course:
            return jsonify({"error": "student or course not found"})
        for course in student.course:
            if course.title == course_title:
                course.score = int(score)
                break
        storage.save()
        return jsonify({"message": "student successfully graded"}), 200