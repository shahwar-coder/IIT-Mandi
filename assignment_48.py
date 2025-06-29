'''
abs:

- `abs()` is a built-in Python function that returns the **absolute value** of a number.
- The absolute value of a number is its non-negative value — it removes any negative sign.
- Syntax: `abs(x)`
- Works with:
  - `int` → e.g. abs(-5) → 5
  - `float` → e.g. abs(-3.14) → 3.14
  - `complex` → returns the magnitude (i.e., modulus) of the complex number
- For a complex number `a + bj`, `abs()` returns √(a² + b²)
- Does **not** modify the original value; returns a new value.
- Raises `TypeError` if the argument is not a number or complex-like object.
'''

print(abs(-10))         # 10 → int input
print(abs(-3.5))        # 3.5 → float input
print(abs(7))           # 7 → already positive
print(abs(0))           # 0 → edge case
print(abs(3 + 4j))      # 5.0 → √(3² + 4²)

