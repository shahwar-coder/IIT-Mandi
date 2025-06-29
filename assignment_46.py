# Solve:

class Student:
    def __init__(self, name):       # Constructor is called when an object is created
        self.name = name            # Stores the name in the instance

    def greet(self):                # Instance method
        return f"Hello, {self.name}!"  # Uses self to access the stored name

'''
- `s = Student("Alice")`  
  → Calls the `__init__` method.  
  → `self.name` is set to `"Alice"` in the new object.

- `s.greet()`  
  → Calls the `greet` instance method.  
  → Returns the string: "Hello, Alice!" by accessing `self.name`.
'''
