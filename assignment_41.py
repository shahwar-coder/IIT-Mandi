'''
self:

- `self` is a reference to the current instance of the class.
- It must be the first parameter of instance methods in Python (including `__init__`).
- It allows access to instance variables and other methods within the class.
- The name `self` is a convention, not a keyword; you could name it differently, but it's discouraged.
- Through `self`, each object maintains its own state (i.e., its own copy of instance variables).
- Without `self`, variables and methods would be shared across instances, leading to incorrect behavior.
- `self` differentiates between class variables and instance variables when names overlap.
'''

# Example:
class Car:
    def __init__(self, brand):
        self.brand = brand  # instance variable assigned via self

    def show(self):
        print(f"This car is a {self.brand}.")

my_car = Car("Toyota")
my_car.show()


'''
- `my_car = Car("Toyota")`
  → Triggers `__init__` with `self` referring to the new object and brand = "Toyota".
  → Inside `__init__`, `self.brand = "Toyota"` binds that value to the object.

- `my_car.show()`
  → Calls the `show` method with `self` referring to `my_car`.
  → Accesses `self.brand`, which is "Toyota", and prints:
    "This car is a Toyota."
'''
