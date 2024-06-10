# Problem: Create a class Employee with attributes name and salary. 
# Add a class method set_raise_percentage to set the raise percentage for all employees, 
# and a static method is_workday that returns True if the given day is a workday (Monday to Friday).

class Employee:
    raise_percentage = 0.03

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self):
        self.salary += self.salary * self.raise_percentage

    @classmethod
    def set_raise_percentage(cls, percentage):
        cls.raise_percentage = percentage
        
        
    @staticmethod
    def is_workday(day):
        return day.weekday() < 5
    
    
import datetime

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

Employee.set_raise_percentage(0.05)
emp1.apply_raise()
emp2.apply_raise()
print(f"New salary for {emp1.name}: {emp1.salary}")
print(f"New salary for {emp2.name}: {emp2.salary}")

workday = datetime.date(2024, 6, 10)
print(f"Is {workday} a workday? {Employee.is_workday(workday)}")
    