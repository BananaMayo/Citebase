from entities.book import Book

def import_from_file(path):
    f = open(path, "r")
    lines = f.readlines()

    books = []

    for i, line in enumerate(lines):
        if line.startswith('@book'):
            title = lines[i + 1][10:][:-3]
            author = lines[i + 2][11:][:-3]
            year = lines[i + 3][9:][:-3]
            publisher = lines[i + 4][14:][:-3]
            book = Book(title, author, year, publisher)
            books.append(book)

    return books


if __name__ == "__main__":
    print(import_from_file(input("path: ")))