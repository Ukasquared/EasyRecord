from ..views import app_routes
from api.views.role import role_required
from flask import request, jsonify, abort
from api.auth import Auth
# register a course - endpoint

@role_required('admin')
@app_routes.route('/register_a_course', methods=['POST'], strict_slashes=False)
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
            try:
                course_id = Auth.register_course(admin_id, teacher_id)
                return jsonify({"course_id": course_id}), 200
            except ValueError:
                abort(404)
