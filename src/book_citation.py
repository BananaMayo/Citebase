

class BookCitation:
    def __init__(self, title, year, author, publisher):
        self.title = title
        self.year = year
        self.author = author
        self.publisher = publisher

    def save_citation(self):
        print('sitation saved')
    
    def __repr__(self) -> str:
        return self.title