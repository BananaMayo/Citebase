import os
import sqlite3
from config import DB_FILE_PATH

dirname = os.path.dirname(__file__)
connection = sqlite3.connect(DB_FILE_PATH)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection