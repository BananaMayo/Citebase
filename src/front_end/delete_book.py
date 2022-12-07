from services.citation_service import citation_services


def delete_book(io, services=citation_services):
    title = io.input('Title: ')

    result = services.delete_book(title)
    io.print(result)
