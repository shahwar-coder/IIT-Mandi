'''
🧠 PROBLEM STATEMENT:
Given a 2D list `arr` of size `N x M`, count and print the total number of **prime numbers** present in the matrix.

✅ Examples:

>>> arr = [
...     [2, 4, 5],
...     [6, 7, 9]
... ]
>>> solve(2, 3, arr)
3

Explanation:
- Prime numbers in the matrix: 2, 5, 7 → count = 3

📝 Assumptions:
- A prime number is an integer greater than 1 that has no positive divisors other than 1 and itself.
- Matrix may contain duplicate or non-positive numbers.
'''

def solve(N, M, arr):
    import math

    def is_prime(n):
        # Prime numbers are greater than 1
        if n < 2:
            return False
        # 2 is the only even prime
        if n == 2:
            return True
        # Exclude other even numbers
        if n % 2 == 0:
            return False
        # Check only odd divisors up to √n
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    prime_count = 0

    # Traverse each element of the matrix
    for row in arr:
        for num in row:
            if is_prime(num):
                prime_count += 1

    print(prime_count)
