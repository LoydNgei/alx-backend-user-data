#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def flask_app() -> str:
    """The JSON route"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register_users() -> str:
    """Register users route"""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
