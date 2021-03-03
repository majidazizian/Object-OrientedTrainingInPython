from abc import ABC, abstractmethod

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def clacArea(self):
        pass

class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def clacArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return f"{{\"Circle\" : {str(self.clacArea())} }}"


c = Circle(10)
print(c.clacArea())
print(c.toJSON())


