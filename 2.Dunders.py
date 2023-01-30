class Book:
    def __init__(self, title, author, book_type, pages):
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages


    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.book_type}', {self.pages})"


    # def __str__(self):
    #     return f"the author of {self.title} is {self.author}"

    def __format__(self, format_spec):
        if format_spec == "short":
            return f"{self.title} - {self.title}"
        elif format_spec == "caps":
            self.title = self.title.upper()
            self.author = self.author.upper()
            self.book_type = self.book_type.upper()
            return self.title


b = Book('the child within', 'Savvas', 'literatur', 400)
print(b.author)