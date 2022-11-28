from services.citation_service import citation_services


def list_book_titles(io):
    titles = citation_services.show_books()
    io.print('\n'.join(titles))
