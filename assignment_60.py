'''
🧠 What is Early Binding?

Early Binding means that the method or function to be called is decided at **compile time**, not at runtime.

✅ In Python, variable names used inside functions are "bound" to their values when the function is defined, not when it's called. This is what we call early binding.

📌 Example:

def make_multiplier(x):
    def multiplier(n):
        return x * n
    return multiplier

times3 = make_multiplier(3)
print(times3(5))  # Output: 15

Here, `x` is early bound inside `multiplier`. Even if you change `x` later, it won’t affect the result.

🧪 If Python used late binding here, changing `x` later could change the result of the function — but it doesn’t!

So, Python uses early binding in closures for variables from outer scopes.
'''
