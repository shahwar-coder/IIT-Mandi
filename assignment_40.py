'''
__init__:

- `__init__` is the constructor method in Python classes.
- It is automatically called when a new object of the class is created.
- The first parameter must always be `self` (refers to the instance being created).
- Used to initialize instance variables (object state).
- It is not mandatory in a class, but useful for custom initialization.
- Can accept additional arguments to set up the object with specific data.
- Cannot return anything other than `None`.
- Overloading `__init__` is not directly supported; use default or variable arguments instead.
'''

# Example:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# Object creation
p = Person("Alice", 25)
p.greet()


'''
- `p = Person("Alice", 25)`
  → Creates a new instance of `Person`.
  → Automatically calls `__init__` with `self`, "Alice", and 25 as arguments.

- Inside `__init__`:
  → `self.name = "Alice"` assigns the name.
  → `self.age = 25` assigns the age.
  → Object `p` now holds these attributes.

- `p.greet()` is called:
  → It accesses `self.name` and `self.age`.
  → Prints: "Hi, I'm Alice and I'm 25 years old."
'''



