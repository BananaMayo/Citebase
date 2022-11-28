from services.citation_service import citation_services


def book_citation(io):
    title = io.input('Title: ')
    author = io.input('Author: ')
    year = io.input('Year: ')
    publisher = io.input('Publisher: ')

    result = citation_services.create_book(title, author, year, publisher)
    io.print(result)
