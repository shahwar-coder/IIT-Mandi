'''
🦆 Duck Typing in Python

🔸 "If it looks like a duck and quacks like a duck, it's a duck."

Python uses **duck typing**, which means:
➡️ The type or class of an object is less important than the methods or behavior it supports.

✔️ If an object implements the required method or behavior, it can be used — regardless of its actual type.

---

✅ Example:

'''

class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_it_quack(thing):
    # We don't care what 'thing' is, as long as it has a .quack() method
    thing.quack()

duck = Duck()
person = Person()

make_it_quack(duck)     # Output: Quack!
make_it_quack(person)   # Output: I'm quacking like a duck!

'''
🔹 No need for explicit interfaces or base classes.
🔹 Focus on behavior, not inheritance.

🛠️ When to use:
- When you expect behavior, not a specific type.
- For flexible and dynamic code.

⚠️ Downside:
- May raise runtime errors if expected method is missing.
- You can check with `hasattr(obj, "method_name")` if needed.

Duck typing enables Python's clean, readable, and dynamic style.
'''
