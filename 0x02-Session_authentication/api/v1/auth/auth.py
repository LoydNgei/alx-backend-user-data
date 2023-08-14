#!/usr/bin/env python3
"""Class to manage the API authentication"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Class name auth that takes in public methods"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method require_auth"""
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        for ex_path in excluded_paths:
            if ex_path.startswith(path):
                return False
            elif path.startswith(ex_path):
                return False
            elif ex_path[-1] == "*":
                if path.startswith(ex_path[:-1]):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """Method authorization header"""
        if request is None:
            return None

        header = request.headers.get('Authorization')

        if header is None:
            return None

        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """Method Current user"""
        return None

    def session_cookie(self, request=None):
        """Method that returns a cookie value from a request"""
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
