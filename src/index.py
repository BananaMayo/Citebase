from front_end.new_citation import book_citation
from front_end.list_citation import list_book_titles


def main():
    while True:
        user_input = input('next command (new book, list books, exit): ')

        if user_input == 'exit':
            break

        if user_input == 'new book':
            book_citation()
        
        if user_input == "list books":
            list_book_titles()


if __name__ == '__main__':
    main()
