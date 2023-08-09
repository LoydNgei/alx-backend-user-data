#!/usr/bin/env python3
"""Class to manage the API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class name auth that takes in public methods"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method require_auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """Method authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Method Current user"""
        return None
