#!/usr/bin/env python3
"""Flask views that handle all routes for the session Auth"""
from api.v1.views import app_views
from flask import request, jsonify
import os
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth():
    """Validate the whole login process"""
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or email == '':
        return jsonify({"error": "email missing"}), 400
    if password is None or password == '':
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})
    if not user or user == []:
        return jsonify({"error": "no user found for this email"}), 404
    for users in user:
        if users.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            result = jsonify(users.to_json())
            session_name = os.getenv('SESSION_NAME')
            result.set_cookie(session_name, session_id)
            return result
    return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def session_logout():
    """Logout from a session"""
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    os.abort(404)
