'''
@classmethod:

- `@classmethod` is a built-in decorator that transforms a method into a **class method**.
- Unlike instance methods (which receive `self`), class methods receive `cls` as the first argument.
- `cls` refers to the class itself, not the instance.
- Can be called on both the **class** and an **instance**, but it always operates on the class level.
- Useful for:
  - Creating **alternative constructors** (`cls(...)`)
  - Accessing or modifying **class variables**
  - Defining **behavior that applies to the class**, not just to instances
- Class methods can return instances or work with class attributes — making them useful for inheritance and factories.
'''

class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @classmethod
    def update_pi(cls, new_pi):
        cls.pi = new_pi

