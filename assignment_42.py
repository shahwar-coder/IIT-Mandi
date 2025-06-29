'''
class Car:
    wheels = 4

my_car = Car()
print("Car wheels:", my_car.wheels)
'''

# Output:

'''
Car wheels: 4
'''

class Car:
    wheels = 4  # Class variable (shared by all instances)

my_car = Car()  # Creates an instance of Car
print("Car wheels:", my_car.wheels)  # Accesses the class variable via the instance
