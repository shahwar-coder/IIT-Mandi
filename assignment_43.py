'''
@staticmethod:

- `@staticmethod` is a decorator used to define a method that belongs to the class, but does **not** use `self` or `cls`.
- It behaves like a regular function but lives in the class’s namespace.
- Does **not** require an instance or class reference to run.
- Useful for utility/helper functions related to the class, but not tied to instance or class state.
- Can be called using either `ClassName.method()` or `instance.method()`.
- Defined with no `self` or `cls` as the first argument.
- It cannot access or modify instance (`self`) or class (`cls`) variables directly.
'''

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Call using class
print(MathUtils.add(3, 5))  # Output: 8

# Call using instance
mu = MathUtils()
print(mu.add(10, 7))        # Output: 17

'''
- `MathUtils.add(3, 5)` calls the `add` method without needing an instance.
- Internally, the method just adds two numbers and returns the result.
- It doesn't depend on object or class state — hence, it's a static method.
- You can also call it with an instance (`mu.add()`), but that still does not pass `self` — Python knows it's static.
'''
