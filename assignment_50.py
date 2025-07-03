'''
MULTIPLE INHERITENCE:

🔹 Multiple Inheritance in Python

- **Multiple Inheritance** means a class can inherit from **more than one parent class**.
- Python allows it directly using this syntax:

    class Child(Parent1, Parent2):
        ...

🔸 How it Works:
- The child class inherits **attributes and methods** from all specified parent classes.
- Python uses **Method Resolution Order (MRO)** to decide which method to execute if there are conflicts (e.g., same method name in multiple parents).
- MRO follows the **C3 linearization** algorithm.

🔸 Use `super()` carefully in multiple inheritance, as it respects MRO.
- View the MRO using:
    `Child.__mro__` or `help(Child)`

🔸 Pros:
- Reuse multiple components.
- More modular code.

🔸 Cons:
- Can be complex and hard to maintain if not used carefully.
- Naming conflicts or method ambiguity may arise.

🔸 Best Practice:
- Always use `super()` in base classes if you expect to be part of multiple inheritance chains.
'''


# Simple Example:

class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):  # Multiple inheritance
    pass

obj = C()
obj.greet()  # Output: Hello from A (because A is first in MRO)
