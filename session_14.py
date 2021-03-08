from dataclasses import dataclass, field
import random

def pages_func():
    return random.randint(51, 2500)

@dataclass
class Book:

    title : str  = "No Title"
    author : str = "No Author"
    pages : int = field(default_factory=pages_func)
    price : float = field(default=10.00)

    
        
 
    
b1 = Book()
print(b1)

b1 = Book("War and Peace", "Leo Tolstoy")
b2 = Book("1984", "Jorj Orvel")

print(b1)
print(b2)
