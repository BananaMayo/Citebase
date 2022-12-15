class Book:
    def __init__(self, title, author, year, publisher):
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher

    def __repr__(self):
        return f'{self.title:34}{self.author:20}{self.year:6}{self.publisher:20}'
