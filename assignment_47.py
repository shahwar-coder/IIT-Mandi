'''
- `isinstance()` is a built-in Python function used to check if an object is an instance of a specified class or a tuple of classes.
- Syntax: `isinstance(object, class_or_tuple)`
- Returns `True` if the object is an instance (or subclass instance) of the given class(es), else returns `False`.
- Works with user-defined classes, built-in types, and abstract base classes.
- Supports inheritance: if the object is an instance of a subclass of the specified class, it still returns `True`.
- Safer than comparing types directly using `type(obj) == SomeClass` because it supports inheritance chains.
- You can pass a tuple of types to check against multiple classes at once.
'''

# Built-in types
print(isinstance(5, int))            # True: 5 is an integer
print(isinstance(5.0, int))          # False: 5.0 is a float, not an int
print(isinstance("hello", str))      # True: "hello" is a string
print(isinstance([1, 2, 3], list))   # True: it’s a list
print(isinstance((1, 2), tuple))     # True: it’s a tuple
print(isinstance({1, 2}, list))      # False: it's a set, not a list

# Multiple types in a tuple
print(isinstance(3.14, (int, float)))   # True: 3.14 is a float, which is in the tuple
print(isinstance("abc", (list, dict)))  # False: it's a string, not a list or dict

# Custom classes and inheritance
class Vehicle: pass
class Car(Vehicle): pass
class Bike: pass

v = Vehicle()
c = Car()
b = Bike()

print(isinstance(v, Vehicle))      # True: v is a Vehicle
print(isinstance(c, Vehicle))      # True: Car is a subclass of Vehicle
print(isinstance(b, Vehicle))      # False: Bike does not inherit from Vehicle
print(isinstance(c, Car))          # True: c is a Car instance
print(isinstance(c, (Car, Bike)))  # True: c is a Car, which is in the tuple

# Edge cases
print(isinstance(None, type(None)))    # True: None is instance of NoneType
print(isinstance(True, bool))          # True: True is a boolean
print(isinstance(True, int))           # True: bool is a subclass of int in Python
print(isinstance("123", int))          # False: it's a string, not an int


# Tawajju Dein:
print(isinstance(c, (Car, Bike)))  # True: c is a Car, which is in the tuple
'''
- In the expression `isinstance(c, (Car, Bike))`, the second argument `(Car, Bike)` is a **tuple of types**.
- Python allows you to pass a tuple to `isinstance()` to check if the object matches **any one** of the types inside.
- This is functionally equivalent to: `isinstance(c, Car) or isinstance(c, Bike)`.
- Python will return `True` as soon as it finds a matching type in the tuple.
- In this case, `c` is an instance of `Car`, so `isinstance(c, Car)` is True.
- Therefore, even though `isinstance(c, Bike)` is False, the overall result is `True` because at least one match is found.
- This is a concise way to check against multiple types at once.
'''
