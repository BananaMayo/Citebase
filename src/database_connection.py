import os
import sqlite3
from config import DB_FILE_PATH
from config import DB_FILE_PATH_TEST

dirname = os.path.dirname(__file__)
connection = sqlite3.connect(DB_FILE_PATH)
test_connection=sqlite3.connect(DB_FILE_PATH_TEST)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection

def get_test_database_connection():
    return test_connection
