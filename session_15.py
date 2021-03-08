from dataclasses import dataclass, field


@dataclass(frozen=True)
class ImmutableClass:
    value1 : str = "value 1"
    value2 : int = 0

    def someFunc(self , newVal):
        self.value2 = newVal

obj = ImmutableClass()
print(obj.value1)

obj.value1 = "value"
obj.someFunc(20)