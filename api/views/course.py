from ..views import app_routes
from api.views.role import role_required
from flask import request, jsonify
from api.auth import Auth
# register a course - endpoint

auth = Auth()



@app_routes.route('/register_a_course', methods=['POST'], strict_slashes=False)
@role_required('admin')
def register_course():
    """enroll teacher into
    a course"""
    # request should contain teacher id, admin id
    # check if course already exist
    if request.method == "POST":
        data = request.get_json()
        if data:
            teacher_id = data.get("teacher_id")
            admin_id = data.get("admin_id")
            title = data.get('title')
            try:
                course_id = auth.register_course(admin_id, teacher_id, title)
                return jsonify({"course_id": str(course_id)}), 200
            except ValueError:
                return jsonify({"error": "Course already registered"}), 400
        return jsonify({"error": "missing or invalid json file"}), 400
