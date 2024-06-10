# Problem: Create a class Student that inherits from the Person class. Add an attribute student_id and a 
# method introduce that includes the student ID in the introduction.

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and my student ID is {self.student_id}.")


student1 = Student('Zoro', 21, 1001)
student1.introduce()