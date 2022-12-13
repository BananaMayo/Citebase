import unittest
from services.citation_service import citation_services
from repositories.citation_repository import CitationRepository
from entities.book import Book
from database_connection import get_test_database_connection
from initialize_database import initialize_test_database
from bib_file_importer import import_from_file


class TestCitations(unittest.TestCase):
    def setUp(self):
        self.testrepo=CitationRepository(get_test_database_connection())
        self.testservices=citation_services
        self.book_1=Book("Harry Potter","Rowling","2000","Otava")
        self.book_2=Book("Taru sormusten herrasta","Tolkien","2022","Otava")
        self.book_3=Book("Muumipeikko ja pyrstötähti","Tove Jansson","2000","Otava")
        self.book_4=Book("Muumipeikko ja pyrstötähti","Tove Jansson","abc","Otava")
        self.book_5=Book("","Tove Jansson","2000","Otava")
        self.book_6=Book("Muumipeikko ja pyrstötähti","","abc","Otava")
        self.book_7=Book("Muumipeikko","Tove Jansson","","Otava")
        self.book_8=Book("Muumipeikko","Tove Jansson","2000","")
        initialize_test_database()


    def test_create_book_citation(self):
        self.testrepo.create_book(self.book_1)
        self.testrepo.create_book(self.book_4)
        test_list=self.testrepo.show_books()
        self.assertEqual(len(test_list), 1)
    
    def test_create_book_empty_inputs(self):
        self.testrepo.create_book(self.book_5)
        self.testrepo.create_book(self.book_6)
        self.testrepo.create_book(self.book_7)
        self.testrepo.create_book(self.book_8)
        test_list=self.testrepo.show_books()
        self.assertEqual(len(test_list), 0)
    
    def test_create_existing_citation(self):
        self.testrepo.create_book(self.book_1)
        self.testrepo.create_book(self.book_1)
        test_list=self.testrepo.show_books()
        self.assertEqual(len(test_list), 1)


    def test_show_books(self):
        self.testrepo.create_book(self.book_1)
        self.testrepo.create_book(self.book_2)
        self.testrepo.create_book(self.book_3)
        books=self.testrepo.show_books()
        self.assertEqual([books[0].title,books[1].title,books[2].title], [self.book_1.title,self.book_2.title,self.book_3.title])

    def test_get_titles(self):
        self.testrepo.create_book(self.book_1)
        self.testrepo.create_book(self.book_2)
        titles=self.testrepo.get_titles()
        self.assertEqual(titles,[self.book_1.title,self.book_2.title])

    def test_delete_book(self):
        self.testrepo.create_book(self.book_1)
        self.testrepo.create_book(self.book_2)
        self.testrepo.delete_book(self.book_1.title)
        self.testrepo.delete_book(self.book_5.title)
        self.testrepo.delete_book("Terve")
        test_list=self.testrepo.show_books()
        print(test_list)
        self.assertEqual(len(test_list), 1)

    def test_delete_all_books(self):
        self.testrepo.create_book(self.book_1)
        self.testrepo.create_book(self.book_2)
        self.testrepo.delete_all_books()
        test_list=self.testrepo.show_books()
        self.assertEqual(test_list, [])

    def test_empty_list(self):
        self.testrepo.create_book(self.book_1)
        self.testrepo.delete_all_books()
        test_titles = self.testrepo.show_books()
        self.assertEqual(test_titles, [])

    def test_import(self):
        imported_book = import_from_file("src/tests/resources/test")[0]
        self.assertEqual(imported_book.title, "How to Import")
        self.assertEqual(imported_book.year, "1888")
        self.assertEqual(imported_book.author, "Myself")
        self.assertEqual(imported_book.publisher, "HY")