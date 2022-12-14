import os
from front_end.new_citation import book_citation
from front_end.list_citation import list_book_titles
from front_end.list_commands import list_command_names
from front_end.delete_book import delete_book
from front_end.delete_all import delete_all
from front_end.bibconverter import create_bib_file, import_from_bib_file
from services.citation_service import citation_services

class App:
    def __init__(self, io, services=citation_services):
        self.io = io
        self.services = services

    def run(self):
        os.system("clear")
        print("\u001b[1;35mWelcome to Citebase!")
        print("\u001b[0mType help to list possible commands")
        while True:
            user_input = self.io.input("\u001b[0m>")
            if user_input == "help":
                os.system("clear")
                list_command_names(self.io)

            if user_input == 'exit':
                os.system("clear")
                break
            if user_input == 'new book':
                os.system("clear")
                book_citation(self.io, self.services)
            if user_input == "list books":
                os.system("clear")
                list_book_titles(self.io, self.services)
            if user_input == "delete book":
                os.system("clear")
                delete_book(self.io, self.services)
            if user_input == "delete all":
                os.system("clear")
                delete_all(self.io, self.services)
            if user_input == "export":
                os.system("clear")
                create_bib_file(self.io, self.services)
            if user_input == "import":
                os.system("clear")
                import_from_bib_file(self.io, self.services)
