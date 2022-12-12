from entities.book import Book

f = open("biblio.bib","r")
lines = f.readlines()
print(lines)

books = []

for i in range(0, len(lines)):
    if lines[i].startswith('@book'):
        title = lines[i+1][10:][:-4]
        author = lines[i+2][11:][:-4]
        year = lines[i+3][9:][:-4]
        publisher = lines[i+4][14:][:-3]
        book = Book(title, author, year, publisher)
        books.append(book)
        print(title, author, year, publisher)

print(books)