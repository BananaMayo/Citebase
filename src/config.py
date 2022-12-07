import os

dirname = os.path.dirname(__file__)

DB_FILENAME = "database.sqlite"
DB_FILENAME_TEST="test-database.sqlite"
DB_FILE_PATH = os.path.join(dirname, '..', 'data', DB_FILENAME)
DB_FILE_PATH_TEST=os.path.join(dirname, '..', 'data', DB_FILENAME_TEST)
