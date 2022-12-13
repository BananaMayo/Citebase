from services.citation_service import citation_services

def list_book_titles(io, services=citation_services):
    books = services.show_books()
    if len(books) == 0:
        books = ["\u001b[1;38;5;221mNo book titles!"]
    for book in books:
        io.print(book)
    