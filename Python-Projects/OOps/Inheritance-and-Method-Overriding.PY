# Problem: Create a class Animal with a method make_sound. 
# Create subclasses Dog and Cat that override the make_sound method to print "Woof" and "Meow" respectively.

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.make_sound()
