class Book:
    def __init__(self,title,author,isbn):
        self._title=title
        self.author=author
        self._isbn=isbn
        self.isAvailable=True

    def borrowBook(self):
        if not self.isAvailable:
            return False
        self.isAvailable = False
        return True

    def returnBook(self):
        self.isAvailable = True

    def displayinfo(self):
        status = "Avaliable" if self.isAvailable else "Not Avaliable"
        print(f"{self._title} by {self.author} ({self._isbn}) is {status}")

book = Book("The Pragmatic Programmer", "David Thomas", "978-0135957059")
book.borrowBook()
book.displayinfo()
book.returnBook()

    