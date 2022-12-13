from services.citation_service import citation_services
from entities.book import Book

def list_book_titles(io, services=citation_services):
    titles = services.show_books()
    if len(titles) == 0:
        titles = ["No book titles!"]
    for i in titles:
        io.print(Book(i[0],i[1],str(i[2]),i[3]))
    io.print(" ")
    