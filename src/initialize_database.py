from database_connection import get_database_connection
from database_connection import get_test_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS Books;")

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE Books (title TEXT PRIMARY KEY, author TEXT, year INTEGER, publisher TEXT);")


    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)

def initialize_test_database():
    connection=get_test_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()