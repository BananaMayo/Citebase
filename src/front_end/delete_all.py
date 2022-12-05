from services.citation_service import citation_services

def delete_all(io):
    result = citation_services.delete_all()
    io.print(result)