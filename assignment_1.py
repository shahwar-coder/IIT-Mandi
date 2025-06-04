# 🧠 PROBLEM STATEMENT:
# Given three numbers `a`, `b`, and `c`, print the smallest (minimum) among them.
#
# ✅ Input:
# - Three integers or floats: a, b, and c
#
# ✅ Output:
# - Print the minimum value among the three inputs
#
# 🧪 Examples:
# >>> minimumOfThree(5, 2, 9)
# 2
#
# >>> minimumOfThree(7, 7, 3)
# 3
#
# >>> minimumOfThree(4, 4, 4)
# 4

def minimumOfThree(a, b, c):
    # Start by assuming the first number is the smallest
    minimum = a

    # Compare with the second number
    if b < minimum:
        minimum = b

    # Compare with the third number
    if c < minimum:
        minimum = c

    # Print the smallest value
    print(minimum)

# OR simply: `print(min(a, b, c))`
