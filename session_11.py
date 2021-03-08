class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        
 
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

b1 = Book("War and Peace", "Leo Tolstoy",39.0)
b2 = Book("1984", "Jorj Orvel",49.40)


print(b1)
b1("Book 1", "M Azizian", 54.5)
print(b1)
