import unittest
from services.citation_service import citation_services
from repositories.citation_repository import CitationRepository
from entities.book import Book
from database_connection import get_test_database_connection
from initialize_database import initialize_test_database


class TestCitations(unittest.TestCase):
    def setUp(self):
        self.testrepo=CitationRepository(get_test_database_connection())
        self.testservices=citation_services
        self.book_1=Book("Harry Potter","Rowling",2000,"Otava")
        self.book_2=Book("Taru sormusten herrasta","Tolkien",2022,"Otava")
        self.book_3=Book("Muumipeikko ja pyrstötähti","Tove Jansson",2000,"Otava")
        initialize_test_database()


    def test_create_book_citation(self):
        test= self.testrepo.create_book(self.book_1)
        self.assertEqual(test, "Citation added successfully")

    
    def test_show_books(self):
        self.testrepo.create_book(self.book_1)
        self.testrepo.create_book(self.book_2)
        self.testrepo.create_book(self.book_3)
        books=self.testrepo.show_books()
        print(books)
        self.assertEqual(books, ["Harry Potter","Taru sormusten herrasta","Muumipeikko ja pyrstötähti"])