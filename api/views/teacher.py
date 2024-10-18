#!/usr/bin/python3
from flask import request, abort, jsonify
from api.views import app_routes
from api.views.role import role_required
from api.models import storage
from api.models.teacher import Teacher
#fetch the teachers details from the database
# fetch the courses they teach
# fetch the names of student offering their course
upload_folder = '/api/files/'


@app_routes.route('/teachers_dashboard', methods=['POST'], strict_slashes=False)
@role_required
def teachers_dashboard():
    if request.method == "POST":
        data = request.get_json()
        if not data:
            abort(407)
        try:
            email = data.get('email')
            if email:
                teacher = storage.find_user(Teacher, email=email)
                student_list = []
                for student in teacher.student:
                    student_names = [student.firstname, student.lastname]
                    student_list.append(student_names)

                user_data = {"teacher": {
                        'id':  teacher.id,
                        'firstname': teacher.firstname,
                        'lastname': teacher.lastname,
                        "email": teacher.email,
                        "gender": teacher.gender,
                        "photo": f"{upload_folder}{teacher.photo}",
                        "course": teacher.course.title,
                    }, "students": student_list 
                    }
                return jsonify(user_data), 200
        except:
            abort(500)
