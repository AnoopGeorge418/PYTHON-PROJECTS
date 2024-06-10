# Problem: Create a base class Shape with a method area. Create subclasses Rectangle and Circle 
# that implement the area method.

import math

class shape:
    def are(self):
        pass 
    
class Rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height 
    
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
shapes = [Rectangle(4, 5), Circle(3)]

for shape in shapes:
    print(shape.area())