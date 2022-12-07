#Bibtex:in luonti 
from services.citation_service import citation_services

def create_bib_file(io):
    result = citation_services.create_bib()
    io.print(result)



