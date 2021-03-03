class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__message = "####"

    def getPrice(self):
        if hasattr(self, "_discount"):
            self.__message = self._discount
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setDiscount(self, amount):
        self._discount = amount


class Newspaper:
    def __init__(self, name):
        self.name = name

b1 = Book("Book 1", "Majid Azizian", 1256, 39.99)
b2 = Book("Book 2", "Aty Iman", 1010, 29.57)
n1 = Newspaper("N 1")
n2 = Newspaper("N 2")

print(isinstance(b1, Book))
print(isinstance(b2, Newspaper))
print(isinstance(n2, object))

print("=" * 50)

print(b1.getPrice(), end="\t")
print(b1.getPrice(), end="\t\t")
print(b1._Book__message)
print(b2.getPrice(), end="\t")
b2.setDiscount(0.35)
print(b2.getPrice(), end="\t\t")
print(b2._Book__message)
