import re
from entities.book import Book

def extract_item(target, bib_item):
    pattern = f"""(?<={target} = ['"{{])[^\'"}}]*(?=['"}}])"""
    return re.search(pattern, bib_item).group(0)

def import_from_file(path):
    f = open(path, "r")
    lines = f.readlines()

    books = []

    for bib in "".join(lines).split("@")[1:]:
        title = extract_item("title", bib)
        author = extract_item("author", bib)
        year = extract_item("year", bib)
        publisher = extract_item("publisher", bib)
        book = Book(title, author, year, publisher)
        books.append(book)

    return books
