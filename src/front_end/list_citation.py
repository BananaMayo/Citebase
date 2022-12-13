from services.citation_service import citation_services

def list_book_titles(io, services=citation_services):
    books = services.show_books()
    if len(books) == 0:
        books = ["No book titles!"]
    for book in books:
        io.print(book)
    io.print(" ")
    