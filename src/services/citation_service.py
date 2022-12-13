from repositories.citation_repository import citation_repository as default_citation_repository
from entities.book import Book
from bib_file_importer import import_from_file


class CitationServices:
    def __init__(self, citation_repository= default_citation_repository):
        self._citation_repository= citation_repository

    def create_book(self, title, author, year, publisher):
        book = self._citation_repository.create_book(Book(title, author, year, publisher))
        return book

    def show_books(self):
        return self._citation_repository.show_books()

    def delete_book(self, title):
        book = self._citation_repository.delete_book(title)
        return book

    def delete_all(self):
        delete = self._citation_repository.delete_all_books()
        return delete

    def create_bib(self):
        bib = self._citation_repository.bib_file()
        return bib

    def import_from_bib_file(self, path):
        imported_books = import_from_file(path)
        if imported_books:
            for book in imported_books:
                self._citation_repository.create_book(book)
            return True

        return False


citation_services = CitationServices()
