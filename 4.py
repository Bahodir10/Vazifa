class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_details(self):
        pass

class Book(LibraryItem):
    def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self.isbn = isbn

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("ISBN:", self.isbn)

class DVD(LibraryItem):
    def __init__(self, title, author, director):
        super().__init__(title, author)
        self.director = director

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Director:", self.director)

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
dvd1 = DVD("Inception", "Christopher Nolan", "Christopher Nolan")

book1.display_details()
print()
dvd1.display_details()
