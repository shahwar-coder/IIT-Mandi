'''
cls:

- `cls` refers to the **class itself**, just like `self` refers to the **instance** of the class.
- It is used inside class methods, which are defined using the `@classmethod` decorator.
- The first parameter of a class method must be `cls` (by convention), though the name can technically be anything.
- Through `cls`, class methods can **access or modify class-level variables**.
- Class methods can act as **alternative constructors** or **factories**, returning new instances of the class.
- Can be called via either the class itself or any of its instances.
'''

class Book:
    category = "Literature"

    def __init__(self, title):
        self.title = title

    @classmethod
    def with_default_title(cls):
        return cls("Untitled")

    @classmethod
    def set_category(cls, new_category):
        cls.category = new_category

'''
- `Book.with_default_title()` creates a Book object with the title "Untitled" using the class itself via `cls(...)`.
- `Book.set_category("Fiction")` modifies the class variable `category`.
- Any changes made through `cls` affect all instances, unless overridden at the instance level.
'''
