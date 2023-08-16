#!/usr/bin/env python3
"""Class Auth"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> str:
    """Hash password method"""
    salt = bcrypt.gensalt()
    result = bcrypt.hashpw(password.encode('utf-8'), salt)
    return result


def _generate_uuid() -> str:
    """Generate UUID"""
    id = uuid4()
    return str(id)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Method that registers users"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

        else:
            raise ValueError('User {} already exists'.format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """Method that Validates user login"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
