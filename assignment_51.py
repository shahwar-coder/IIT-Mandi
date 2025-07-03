'''
🔹 `super()` in Python

- `super()` is a built-in function used to **call methods from a parent (superclass)**.
- Commonly used inside `__init__()` to initialize the parent class when a child class overrides it.

🔸 Syntax:
    super().method(args)

🔸 Why use `super()`?
- To **avoid hardcoding parent class name**
- Supports **multiple inheritance** and obeys **Method Resolution Order (MRO)**
- Ensures consistent and maintainable code when class hierarchies evolve

🔸 Where `super()` is used:
1. Inside `__init__()` to call parent's constructor
2. Inside any method to reuse logic from parent

🔸 Works with:
- Single inheritance ✅
- Multiple inheritance ✅ (very useful when all classes in chain use `super()`)

🔸 MRO (Method Resolution Order):
- Python decides which class method to call using the MRO
- View using: `ClassName.__mro__`

🔸 Best Practice:
- Always prefer `super()` over calling `Parent.method(self, ...)`
- Especially important in multiple inheritance for cooperative behavior

🔸 Note:
- You can also use `super(CurrentClass, self)` in older Python versions
'''

class Animal:
    def __init__(self):
        print("Animal constructor")

class Dog(Animal):
    def __init__(self):
        super().__init__()      # calls Animal's constructor
        print("Dog constructor")

d = Dog()

# OUTPUT
# Animal constructor
# Dog constructor
