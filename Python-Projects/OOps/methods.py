# Problem: Add a method introduce to the Person class that prints a message introducing the person.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def introuce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
person1 = Person('Luffy', 17)
person1.introuce()