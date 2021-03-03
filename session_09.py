class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
 
    def __eq__(self, value):
       if not isinstance(value, Book):
           raise ValueError("Can't compare book to a non-book")

       return (self.title == value.title and self.author == value.author and self.price == value.price)
    
    def __ge__(self, value):
        if not isinstance(value, Book):
           raise ValueError("Can't compare book to a non-book")

        return self.price >= value.price
    
    def __lt__(self, value):
        if not isinstance(value, Book):
           raise ValueError("Can't compare book to a non-book")

        return self.price < value.price

    

b1 = Book("War and Peace", "Leo Tolstoy",39.0)
b2 = Book("1984", "Jorj Orvel",49.40)
b3 = Book("War and Peace", "Leo Tolstoy",39.0)

# print(b1 == b2)
# print(b1 == b3)
# print(b1 == 42)

# print(b1 < b2)
# print(b3 >= b2)

books = [b1, b2, b3]
for b in books:
    print(b.title)
books.sort()
print([book.title for book in books])