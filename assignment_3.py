# 🧠 PROBLEM STATEMENT:
# Given three integers `left`, `right`, and `k`, count how many numbers 
# between `left` and `right` (inclusive) are divisible by `k`.
#
# ✅ Input:
# - Integers: left, right (range boundaries), and k (divisor)
#
# ✅ Output:
# - Print the count of numbers divisible by k in the range [left, right]
#
# 🧪 Examples:
# >>> count_numbers_divisible_by_k(1, 10, 2)
# 5
# (Numbers divisible by 2 are: 2, 4, 6, 8, 10)
#
# >>> count_numbers_divisible_by_k(5, 15, 3)
# 4
# (Numbers divisible by 3 are: 6, 9, 12, 15)

def count_numbers_divisible_by_k(left, right, k):
    count = 0
    # Iterate over all numbers from left to right inclusive
    for i in range(left, right + 1):
        # Check divisibility by k
        if i % k == 0:
            count += 1
    print(count)
