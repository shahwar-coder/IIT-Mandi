# 🧠 PROBLEM STATEMENT:
# Given three integers representing the lengths of the sides of a triangle,
# determine whether they can form a **right-angled triangle**.
#
# A triangle is right-angled if the square of the longest side (hypotenuse)
# is equal to the sum of the squares of the other two sides.
#
# ✅ Input:
# - Three integers `a`, `b`, and `c`
#
# ✅ Output:
# - Print "Yes" if the sides form a right-angled triangle, otherwise print "No"
#
# 🧪 Examples:
# >>> Solve(3, 4, 5)
# Yes
#
# >>> Solve(5, 5, 5)
# No

def Solve(a, b, c):
    # Sort the three sides so the largest side is assumed to be the hypotenuse
    sides = sorted([a, b, c])
    x, y, hyp = sides  # x, y: shorter sides; hyp: longest side

    # Check if Pythagorean theorem holds: hyp² == x² + y²
    if hyp**2 == x**2 + y**2:
        print("Yes")  # It's a right-angled triangle
    else:
        print("No")   # Not a right-angled triangle
