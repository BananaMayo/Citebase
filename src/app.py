from front_end.new_citation import book_citation
from front_end.list_citation import list_book_titles
from front_end.delete_book import delete_book
from front_end.delete_all import delete_all


class App:
    def __init__(self, io):
        self.io = io

    def run(self):
        while True:
            user_input = self.io.input('next command (new book, list books, exit, delete book, delete all):')

            if user_input == 'exit':
                break

            if user_input == 'new book':
                book_citation(self.io)

            if user_input == "list books":
                list_book_titles(self.io)
            
            if user_input == "delete book":
                delete_book(self.io)
            
            if user_input == "delete all":
                delete_all(self.io)