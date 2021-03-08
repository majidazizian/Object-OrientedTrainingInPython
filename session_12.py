from dataclasses import dataclass

@dataclass
class Book:

    title : str
    author : str
    pages : int
    price : float

    def bookinfo(self):
        return f"{ self.title } by { self.author }"    
        
 
    

b1 = Book("War and Peace", "Leo Tolstoy", 512, 39.0)
b2 = Book("1984", "Jorj Orvel", 256, 49.40)
b3 = Book("War and Peace", "Leo Tolstoy", 512, 39.0)

print(b1.title)
print(b2.author)

print(b1)

print(b1 == b3)

b3.title = "Anna Karenina"
b3.pages = 768
b3.price = 54.25

print(b3.bookinfo())

print(b1 == b3)

