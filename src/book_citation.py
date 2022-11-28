class BookCitation:
    def __init__(self, title, author, year, publisher):
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher

    def save_citation(self):
        print('citation saved')
    
    def __repr__(self) -> str:
        return self.title