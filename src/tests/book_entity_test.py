import unittest
from entities.book import Book

class BookTest(unittest.TestCase):
    def test_book_repr(self):
        book = Book("How to Book", "Who Is", "1900", "Indie Books Inc.")
        self.assertEqual(book.__repr__(), "How to Book                       Who Is              1900  Indie Books Inc.    ")
