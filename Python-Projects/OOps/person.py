# Problem: Create a class called Person with attributes name and age. 
# Create an object of the class and print the name and age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        
        
person1 = Person('Anoop', 22)
print(f'Im {person1.name} and im {person1.age} years old.')