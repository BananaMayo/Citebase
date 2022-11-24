def main():
    while True:
        user_input = input('next command: ')

        if user_input == '':
            break

        if user_input == 'new book':
            print('new_book_function() called')

if __name__ == '__main__':
    main()
