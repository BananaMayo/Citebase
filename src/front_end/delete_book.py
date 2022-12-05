from services.citation_service import citation_services


def delete_book(io):
    title = io.input('Title: ')

    result = citation_services.delete_book(title)
    io.print(result)