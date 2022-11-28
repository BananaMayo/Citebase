from services.citation_service import citation_services


def book_citation():
    title = input('Title: ')
    author = input('Author: ')
    year = input('Year: ')
    publisher = input('Publisher: ')

    result = citation_services.create_book(title, author, year, publisher)
    print(result)
