class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.author = author
        self.price = price
        self.chapters = []

    def addChapter(self, Chapter):
        self.chapters.append((Chapter))

    def getBookPageCount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result

class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

author = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, author)
b1.addChapter(Chapter("Chapter 1", 125))
b1.addChapter(Chapter("Chapter 2", 97))
b1.addChapter(Chapter("Chapter 3", 143))

print(b1.author)
print(b1.title)
print(b1.getBookPageCount())