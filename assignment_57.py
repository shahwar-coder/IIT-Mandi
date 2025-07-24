'''
📘 Python's abc Module — Abstract Base Classes

The `abc` module allows you to define abstract base classes.

🔹 Abstract Base Class (ABC):
An abstract base class is a class that cannot be instantiated on its own.
It can define abstract methods that *must* be implemented in any subclass.

➡️ abc module provides:
- `ABC`: base class to inherit from.
- `@abstractmethod`: decorator to mark methods that must be overridden.

✅ Example:

'''

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

# ✅ Subclass that implements all abstract methods
class Dog(Animal):
    def speak(self):
        return "Woof!"

    def move(self):
        return "Runs"

dog = Dog()
print(dog.speak())  # Output: Woof!

'''
🛑 If you try to do this:
    a = Animal()  # ❌ Error! Cannot instantiate abstract class
    class Cat(Animal):
        def speak(self): pass
    c = Cat()     # ❌ Error! 'move' not implemented

🧠 Key Points:
- ABCs are useful for defining interfaces or base behavior.
- Enforces consistency across subclasses.
- Helps in large-scale application design.

🔍 abc module promotes cleaner design and better code architecture.
'''
