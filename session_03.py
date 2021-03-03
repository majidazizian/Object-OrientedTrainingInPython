class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Periodical(Publication):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period


class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages
        self.__type = "Book"

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)
        self.__type = "Magazine"

class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)
        self.__type = "Newspaper"

b1 = Book("Book 1", "Author 1", 218, 25.45)
n1 = Newspaper("Newspaper 1", "Publisher 1", 6.50, "Daily")
m1 = Magazine("Magazine 1", "Publisher 2", 14.45, "Monthly")

print(f"Title : {b1.title}, Price : {b1.price}, Author : {b1.author}, Pages : {b1.pages}.")
print(f"Title : {n1.title}, Price : {n1.price}, Publisher : {n1.publisher}, Period : {n1.period}.")
print(f"Title : {m1.title}, Price : {m1.price}, Publisher : {m1.publisher}, Period : {m1.period}.")
