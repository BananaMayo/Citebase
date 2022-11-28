from services.citation_service import citation_services


def book_citation():
    title = input('Title: ')
    author = input('Author: ')
    year = input('Year: ')
    publisher = input('Publisher: ')

    citation_services.create_book(title, author, year, publisher)
