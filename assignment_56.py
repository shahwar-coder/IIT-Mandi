'''
📘 Interface in Python

Python does not have built-in "interfaces" like Java or C#, but you can achieve interface-like behavior using:

1. Abstract Base Classes (ABCs) from the `abc` module.
2. Method definitions that subclasses must override.

👉 Purpose:
An interface defines a set of methods that a class must implement, without providing their actual implementation.

✅ Using `abc.ABC` and `@abstractmethod`:

'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Now any subclass of Shape must implement area() and perimeter()

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

c = Circle(5)
print("Area:", c.area())        # ✅ Works
print("Perimeter:", c.perimeter())

'''
🛑 If you try to create an object of Shape or a subclass without implementing all abstract methods, Python will raise an error.

✅ Why use interfaces?
- To enforce a contract for subclasses.
- To make sure different subclasses follow the same method structure.

Interfaces help in large-scale applications for consistency and maintainability.
'''
