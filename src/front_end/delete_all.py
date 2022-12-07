from services.citation_service import citation_services

def delete_all(io, services=citation_services):
    result = services.delete_all()
    io.print(result)
