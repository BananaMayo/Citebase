from services.citation_service import citation_services

def book_citation():
    title = input('Title: ')
    author = input('Author: ')
    year = input('Year: ')
    publisher = input('Publisher: ')

    #print(title, author, year, publisher)

    citation_services.create_book(title, author, year, publisher)

def show_books():
    titles = citation_services.show_books()
    print('\n'.join(titles))


if __name__ == "__main__":
    book_citation()