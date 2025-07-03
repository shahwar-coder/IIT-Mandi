'''
INHERITENCE:
.
🔹 Inheritance in Python (OOP Concept)

- Inheritance allows a **class (child)** to inherit properties and methods from another **class (parent)**.
- Promotes **code reuse**, **extensibility**, and **modularity**.

🔸 Basic Syntax:
    class Parent:
        ...

    class Child(Parent):
        ...

🔸 Types of Inheritance:
1. **Single Inheritance**:
    - One child inherits from one parent.
2. **Multiple Inheritance**:
    - One child inherits from multiple parents.
3. **Multilevel Inheritance**:
    - Class inherits from a child class which itself inherits from another.
4. **Hierarchical Inheritance**:
    - Multiple child classes inherit from the same parent.
5. **Hybrid Inheritance**:
    - Combination of above types.

🔸 Key Concepts:
- `super()` → Used to call parent class methods/constructors.
- Child class **inherits** all attributes and methods of parent unless overridden.
- You can **override** methods by defining them again in the child class.

🔸 Benefits:
- Reuse code from existing classes.
- Fewer lines of code.
- Logical class relationships.

🔸 Method Resolution Order (MRO):
- Determines the order in which base classes are searched (especially in multiple inheritance).
- Use `ClassName.__mro__` or `help(ClassName)` to view it.

🔸 Constructor Chaining:
- If child has `__init__()`, parent’s `__init__()` won't run unless called explicitly via `super()`.

🔸 Best Practice:
- Always use `super()` to refer to parent members (especially for maintainability and multiple inheritance).
'''

# Inheritence example (Single Inheritence)
class Animal:
    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def bark(self):
        return "Woof!"

d = Dog()
print(d.speak())   # inherited from Animal
print(d.bark())    # defined in Dog


# Inheritence with __init__ and super():
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        # Call the constructor of the parent class (Person)
        super().__init__(name)
        # Initialize the additional attribute specific to Student
        self.grade = grade

'''
Explanation:

1. A class `Person` is defined with an `__init__` method that initializes the `name` attribute.

2. Another class `Student` is defined, which inherits from `Person`.

3. The `Student` class has its own `__init__` method that takes two parameters: `name` and `grade`.

4. Inside the `Student` constructor:
   - `super().__init__(name)` calls the `__init__` method of the parent class (`Person`)
     and assigns the `name` to `self.name`.
   - `self.grade = grade` assigns the grade to the student instance.

5. When we create a `Student` object:
   s = Student("Alice", "A")

   - It first sets `self.name = "Alice"` using the parent class constructor.
   - Then it sets `self.grade = "A"` using its own constructor.

6. Finally, printing:
   print(s.name, s.grade)

   Outputs:
   Alice A
'''

s = Student("Alice", "A")
print(s.name, s.grade)


# ==============

# Also see the following visula for strengthening the concept even further.
'''
Student("Alice", "A")
   └── super().__init__("Alice") --> sets self.name = "Alice"
   └── sets self.grade = "A"
'''

# One major benefit of inheritence:
'''
✅ Code Reusability: Inheritance allows a class to reuse the methods and properties of another class,
   reducing duplication and making the code more maintainable and modular.
'''
