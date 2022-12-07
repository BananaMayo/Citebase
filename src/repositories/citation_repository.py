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
        
        if len(titles) == 0:
            titles = "No book titles!"
        
        return titles

    
    def delete_book(self, title):
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Books WHERE title= ?", [title])
        self._connection.commit()

        return "Book removed successfully"

    def delete_all_books(self):
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Books")

        return "All books removed successfully"



citation_repository = CitationRepository(get_database_connection())