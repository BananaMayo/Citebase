from new_citation import book_citation

def main():
    while True:
        user_input = input('next command: ')

        if user_input == '':
            break

        if user_input == 'new book':
            book_citation()

if __name__ == '__main__':
    main()
