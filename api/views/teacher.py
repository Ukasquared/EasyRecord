#!/usr/bin/python3
from flask import request, abort, jsonify
from api.views import app_routes
from api.views.role import role_required
from api.models import storage
from api.models.teacher import Teacher
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
