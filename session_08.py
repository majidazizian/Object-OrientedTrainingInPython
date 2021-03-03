class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, codts {self.price}."

    def __repr__(self):
        return f"title={self.title},author={self.author},price={self.price}"  

    

b1 = Book("War and Peace", "Leo Tolstoy",39.0)
b2 = Book("1984", "Jorj Orvel",49.40)

print(b1)
print(b2)
print(str(b1))
print(repr(b2))