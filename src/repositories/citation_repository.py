from database_connection import get_database_connection


class CitationRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_book(self, book):
        cursor = self._connection.cursor()
        cursor.execute("INSERT into Books (title, author, year, publisher) VALUES (?, ?, ?, ?)", [book.title, book.author, book.year, book.publisher])
        self._connection.commit()
        return 	f"\u001b[32mCitation added successfully"

    def show_books(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Books")
        rows = cursor.fetchall()
        titles = []
        for row in rows:
            titles.append((row[0]))
        return titles

    def delete_book(self, title):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Books WHERE title= ?", [title])
        self._connection.commit()
        return 	f"\u001b[32mBook removed successfully"

    def delete_all_books(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Books")
        self._connection.commit()
        return f"\u001b[32mAll books removed successfully"

    def bib_file(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Books")
        rows = cursor.fetchall()

        books = []

        for row in rows:
            books.append({'title': row[0],
                        'author': row[1],
                        'year': row[2],
                        'publisher': row[3]})

        name = input("Name for bib-file: ")
        file = open(str(name)+'.bib', 'w')

        book_bib = ""
        i = 123123
        brl = '{'
        brr = '}'
        tag = f"@book,{brl}tag{i}"
        for book in books:
            tag = str.lower(str.replace(book["title"], " ", "")) + str(book["year"]) + str(i)
            book_bib = book_bib + f"@book{brl}{tag},\n title = '{book['title']}', \n author = '{book['author']}', \n year = '{book['year']}', \n publisher = '{book['publisher']}',\n{brr}\n\n"
            i = i + 1

        file.write(book_bib)
        file.close()
        return f"\u001b[32mExported successfully"



citation_repository = CitationRepository(get_database_connection())
