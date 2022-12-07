from services.citation_service import citation_services


def book_citation(io, services=citation_services):
    title = io.input('Title: ')
    author = io.input('Author: ')
    year = io.input('Year: ')
    publisher = io.input('Publisher: ')

    result = services.create_book(title, author, year, publisher)
    io.print(result)
