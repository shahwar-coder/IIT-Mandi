'''
What would happen if super().__init__() were omitted in the Developer class?
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        self.programming_language = programming_language
        super().__init__(name, salary)  # This calls the parent class __init__

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")


# Output:

# The `salary` attribute would not be initialized
