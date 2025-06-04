# 🧠 PROBLEM STATEMENT:
# Given a positive integer `num`, print its multiplication table from 1 to 10.
#
# ✅ Input:
# - A positive integer `num`
#
# ✅ Output:
# - Print the result of num multiplied by 1 through 10, each on a new line
#
# 🧪 Example:
# >>> print_multiplication_table(5)
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50

def print_multiplication_table(num):
    # Loop from 1 to 10 (inclusive)
    for i in range(1, 11):
        # Print the result of num * i
        print(num * i)
