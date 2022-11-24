# import bookservice from bookservicefile

def book_citation():
    title = input('Title: ')
    year = input('Year: ')
    author = input('Author: ')
    publisher = input('Publisher: ')

    print(title, year, author, publisher)
    #bookservice.new_book(title, year, author, publisher)


if __name__ == "__main__":
    book_citation()