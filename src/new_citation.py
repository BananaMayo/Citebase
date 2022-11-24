# import bookservice from bookservicefile

def book_citation():
    title = input('Title: ')
    author = input('Author: ')
    year = input('Year: ')
    publisher = input('Publisher: ')

    print(title, author, year, publisher)
    #bookservice.new_book(title, year, author, publisher)


if __name__ == "__main__":
    book_citation()