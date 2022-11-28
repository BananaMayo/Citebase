from services.citation_service import citation_services


def list_book_titles():
    titles = citation_services.show_books()
    print('\n'.join(titles))
