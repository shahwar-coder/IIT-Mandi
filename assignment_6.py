# 🧠 PROBLEM STATEMENT:
# Given a non-negative integer `num`, compute the sum of all even numbers from 1 to `num` (inclusive).
#
# ✅ Input:
# - A single non-negative integer `num`
#
# ✅ Output:
# - Print the sum of all even numbers between 1 and `num` (inclusive)
#
# 🧪 Examples:
# >>> sum_of_even_numbers(10)
# 30
# (Because: 2 + 4 + 6 + 8 + 10 = 30)
#
# >>> sum_of_even_numbers(5)
# 6
# (Because: 2 + 4 = 6)
#
# 💡 Constraint:
# - If `num` is negative, raise an assertion error.

def sum_of_even_numbers(num):
    # Ensure the input is a non-negative number
    assert num >= 0, "Number should be greater than or equal to 0"

    # Use list comprehension to filter even numbers and sum them
    print(sum([n for n in range(1, num + 1) if n % 2 == 0]))
