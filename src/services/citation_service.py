from repositories.citation_repository import CitationRepository as default_citation_repository
from entities.book import Book

class CitationServices:
    def __init__(self, citation_repository= default_citation_repository):
        self._citation_repository= citation_repository

    def create_book(self, title, author, year, publisher):
        book = self._citation_repository.create_book(title, author, year, publisher)
        return book

citation_services = CitationServices()