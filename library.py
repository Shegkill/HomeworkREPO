class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_books_by_author(self, author):
        return [b for b in self.books if b.author == author]

    def get_all_books(self):
        return self.books
