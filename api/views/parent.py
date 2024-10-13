#!/usr/bin/python3
"""parent view function"""
from views import app_routes, role_required
from flask import request

@role_required('parent')
@app_routes.route('/parent_dashboard', strict_slashes=False)
def student_score():
    """returns student
    scores"""
    data = request.get_json()
    if not data:
        return
