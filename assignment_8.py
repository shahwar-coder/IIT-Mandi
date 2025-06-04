# 🧠 PROBLEM STATEMENT:
# Given two integers `min_val` and `max_val`, print all integers from `min_val` up to (but not including) `max_val`.
#
# ✅ Input:
# - Two integers: `min_val` and `max_val`
#
# ✅ Output:
# - Print each integer from `min_val` to `max_val - 1`, one on each line.
#
# 🧪 Examples:
# >>> print_range(3, 7)
# 3
# 4
# 5
# 6
#
# >>> print_range(0, 3)
# 0
# 1
# 2

def print_range(min_val, max_val):
    # Loop through the range from min_val to max_val (exclusive)
    for i in range(min_val, max_val):
        print(i)
