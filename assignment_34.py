'''
🧠 PROBLEM STATEMENT:
Given two integers `num1` and `num2`, return their **Greatest Common Divisor (GCD)** using the Euclidean algorithm.

✅ Example:

>>> findGCD(48, 36)
12

📝 Assumptions:
- Both numbers are non-negative integers (0 or positive)
- GCD of (0, x) is x, and GCD of (0, 0) is undefined (you may add a check for it)
'''

def findGCD(num1: int, num2: int) -> int:
    """Return Greatest Common Divisor using Euclidean algorithm"""
    # Continue until remainder becomes 0
    while num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    return num1

# Test case
print(findGCD(48, 36))  # Output: 12


'''
🧠 EUCLIDEAN ALGORITHM EXPLAINED:

The Euclidean algorithm efficiently computes the Greatest Common Divisor (GCD) of two integers.

📌 Key Idea:
- GCD(a, b) = GCD(b, a % b)
- Keep replacing (a, b) with (b, a % b) until b becomes 0
- At that point, a is the GCD

🔄 Steps:
1. Take two numbers: num1 and num2
2. While num2 is not zero:
    - Set remainder = num1 % num2
    - Update num1 = num2
    - Update num2 = remainder
3. When num2 becomes 0, num1 holds the GCD

✅ Example:
findGCD(48, 36)
→ 48 % 36 = 12 → GCD(36, 12)
→ 36 % 12 = 0  → GCD(12, 0)
→ GCD = 12

🕒 Time Complexity: O(log(min(num1, num2)))
'''
