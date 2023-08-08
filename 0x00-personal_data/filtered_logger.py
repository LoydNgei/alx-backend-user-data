#!/usr/bin/env python3
""" A function called filter_datum that returns the log message obfuscated """
from typing import List
import re
import logging
import os
import mysql.connector


# Fields to be redacted
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Return the log message obfuscated"""

    for x in fields:
        message = re.sub(f'{x}=.*?{separator}',
                         f'{x}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialization method of the class Redacting formatter"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format method that filters values in incoming log records"""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """Func that takes no args and returns a logging_logger obj"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a connector to the database"""
    username = os.getenv("PERSONAL_DATA_DB_USERNAME")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD")
    host = os.getenv("PERSONAL_DATA_DB_HOST")
    name = os.getenv("PERSONAL_DATA_DB_NAME")

    getdb = mysql.connector.connection.MySQLConnection(user=username,
                                                       password=password,
                                                       host=host,
                                                       database=name)
    return getdb
