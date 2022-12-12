from services.citation_service import citation_services


def list_book_titles(io, services=citation_services):
    titles = services.show_books()
    if len(titles) == 0:
        titles = ["No book titles!"]
    io.print('\n'.join(titles))
    io.print(" ")
    