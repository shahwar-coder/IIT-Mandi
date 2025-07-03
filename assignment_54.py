'''
METHOD OVERRIDING:

🔹 Method Overriding in Python

- **Method Overriding** occurs when a **child class defines a method** with the **same name as a method in its parent class**.
- The child class version **replaces** (overrides) the parent class version **when called using a child object**.

🔸 Purpose:
- To provide **customized behavior** in the child class.
- To extend or modify the functionality of the inherited method.

🔸 Syntax:
    class Parent:
        def greet(self):
            print("Hello from Parent")

    class Child(Parent):
        def greet(self):   # overrides Parent's greet()
            print("Hello from Child")

🔸 How to Call the Parent’s Overridden Method:
- Use `super().method_name()` inside the child method to **include** parent logic:
    super().greet()

🔸 Overriding vs Overloading:
- Python **does not support method overloading** (same method with different arguments).
- Python uses **default arguments** or `*args, **kwargs` to simulate overloading.

🔸 Key Rules:
- Method name must match exactly.
- Number and type of arguments can differ.
- Only the **latest override** will be in effect.

🔸 Use Case:
- When a child needs to **customize** or **extend** base behavior.
'''

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()   # Output: Dog barks
