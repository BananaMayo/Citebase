from database_connection import get_database_connection


class CitationRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_book(self, book):
        cursor = self._connection.cursor()

        cursor.execute("INSERT into Books (title, author, year, publisher) VALUES (?, ?, ?, ?)", [book.title, book.author, book.year, book.publisher])
        self._connection.commit()

        return "Citation added successfully"
    
    def show_books(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Books")

        rows = cursor.fetchall()

        titles = []

        for row in rows:
            titles.append((row[0]))
        
        return titles



citation_repository = CitationRepository(get_database_connection())