'''
Output of following code:
'''

class Organism:
    def live(self):
        print("Living...")

class Animal(Organism):
    pass

class Bird(Animal):
    def fly(self):
        print("Flying...")

sparrow = Bird()
sparrow.live()
sparrow.fly()


# Living...
# Flying...
