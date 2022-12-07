import unittest
from unittest.mock import Mock, ANY
from services.citation_service import CitationServices


class TestCitationsService(unittest.TestCase):
    def setUp(self):
        self.repo_mock=Mock()
        self.testservices=CitationServices(self.repo_mock)
        self.book_mock = Mock()
        self.book_mock.title="Kirja"
        self.book_mock.author="Sanni"
        self.book_mock.year=2020
        self.book_mock.publisher="Otava"

    
    def test_create_book(self):
        self.testservices.create_book(self.book_mock.title,self.book_mock.author,self.book_mock.year,self.book_mock.publisher)
        self.repo_mock.create_book.assert_called()

    def test_show_books(self):
        self.testservices.show_books()
        self.repo_mock.show_books.assert_called()

    def test_delete_book(self):
        self.testservices.create_book(self.book_mock.title,self.book_mock.author,self.book_mock.year,self.book_mock.publisher)
        self.testservices.delete_book(self.book_mock.title)
        self.repo_mock.delete_book.assert_called()

    def test_delete_all(self):
        self.testservices.create_book(self.book_mock.title,self.book_mock.author,self.book_mock.year,self.book_mock.publisher)
        self.testservices.delete_all()
        self.repo_mock.delete_all_books.assert_called()

    


