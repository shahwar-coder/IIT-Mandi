# 🧠 PROBLEM STATEMENT:
# Given a positive integer `num`, print all numbers from 1 to `num` (inclusive), one per line.
#
# ✅ Input:
# - A positive integer `num`
#
# ✅ Output:
# - Print the numbers from 1 to `num`, each on a new line.
#
# 🧪 Examples:
# >>> Solve(4)
# 1
# 2
# 3
# 4

def Solve(num):
    # Check if input is a valid positive number
    assert num > 0, "Input must be a positive integer"

    # Loop from 1 to num and print each number
    for n in range(1, num + 1):
        print(n)
