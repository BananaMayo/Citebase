from services.citation_service import citation_services

def create_bib_file(io, services=citation_services):
    result = services.create_bib()
    io.print(result)

def import_from_bib_file(io, services=citation_services):
    path = io.input("path: ")
    services.import_from_bib_file(path)
    print("Import done")
