from database_connection import get_database_connection
from entities.book import Book
#from services.citation_service import citation_services

class CitationRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_book(self,book):
        cursor = self._connection.cursor()

        cursor.execute("INSERT into Book (title, author, year, publisher) VALUES (?, ?, ?, ?)", [book.title, book.author, book.year, book.publisher])
        self._connection.commit()

        return "Citation added successfully"

citation_repository = CitationRepository(get_database_connection())