from front_end.new_citation import book_citation
from front_end.list_citation import list_book_titles


class App:
    def __init__(self, io):
        self.io = io

    def run(self):
        while True:
            user_input = self.io.input('next command (new book, list books, exit): ')

            if user_input == 'exit':
                break

            if user_input == 'new book':
                book_citation(self.io)

            if user_input == "list books":
                list_book_titles(self.io)
