class Book:

    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    __booklist = None

    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPES

    @staticmethod
    def getBookList():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if(not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is nota valid book type")
        else:
            self.booktype = booktype
        

print("Book Types: ", Book.getBookTypes(), "\n")

print("Title", "\t", "Type")
print("=" * 50)
b1 = Book("Book 1", "HARDCOVER")
b2 = Book("Book 2", "EBOOK")

print(b1.title, "\t", b1.booktype)
print(b2.title, "\t", b2.booktype)

print("*" * 100, "\n")
theBooks = Book.getBookList()
theBooks.append(b1)
theBooks.append(b2)
print(theBooks)