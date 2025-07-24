'''
📘 Method Resolution Order (MRO) in Python

🔹 What is MRO?
MRO defines **the order** in which Python looks for a method or attribute in **multiple inheritance**.

🧠 Python uses **C3 Linearization (C3 MRO)** to determine the method resolution order.

✅ Example 1: Simple Multiple Inheritance
'''
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

print(D.__mro__)  # Shows the MRO order of class D
'''
🔎 MRO: D → B → C → A → object
So:
If we call D().show(), it searches in this order: B → C → A
B has show(), so it uses that.
'''

d = D()
d.show()  # Output: B

'''
✅ Example 2: Use of super() with MRO
super() will follow the MRO chain.
'''

class X:
    def show(self):
        print("X")

class Y(X):
    def show(self):
        print("Y")
        super().show()

class Z(X):
    def show(self):
        print("Z")
        super().show()

class P(Y, Z):
    def show(self):
        print("P")
        super().show()

print(P.__mro__)  # (P, Y, Z, X, object)
p = P()
p.show()

'''
🧾 Output:
P
Y
Z
X

🔁 Each call to super() follows the MRO order of class P.

📌 Key Takeaways:
- MRO is used when classes inherit from multiple classes.
- Python follows left-to-right search.
- Use __mro__ or help(ClassName) to see the MRO.

'''
