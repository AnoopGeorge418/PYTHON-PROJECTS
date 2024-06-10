# Problem: Create a class Address with attributes city and zipcode. 
# Create a class Person that includes an Address object as an attribute.

class Address:
    def __init__(self, city, zipcode):
        self.city = city 
        self.zipcode = zipcode
        
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I live in {self.address.city}, {self.address.zipcode}.")
        
address1 = Address('Mangalore', '543421')
person1 = Person('sanji', 21, address1)
person1.introduce()