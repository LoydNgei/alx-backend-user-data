#!/usr/bin/env python3
"""Encrypt Passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Func that returns salted, hashed psswd which is byte str"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Func that checks the validity and returns bool"""
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
