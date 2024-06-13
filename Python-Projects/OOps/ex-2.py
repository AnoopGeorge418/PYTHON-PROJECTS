#  Number Served: Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and print
# the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a day of
# business.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f'Name of the Restaurant: {self.restaurant}')
        print(f'Cuisine type: {self.cuisine}')
        
    def open_restaurant(self):
        return 'Restaurant is Open.'
    
    def set_number_served(self):
        print(f'{self.number_served} people got served')
        
    def increment_number_served(self, n_peoples):
        self.number_served += n_peoples
        

# creating instance
restaurant = Restaurant('The Great kitchen', 'Chinese')
print(restaurant.number_served)
restaurant.number_served = 25
print(restaurant.set_number_served())
print(restaurant.increment_number_served(100))
print(restaurant.set_number_served())

print('\n')

# Login Attempts: Add an attribute called login_attempts to your User class
# from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
# that increments the value of login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

class users:
    def __init__(self, first_name, last_name, password, login_attempts):
        self.f_name = first_name
        self.l_name = last_name
        self.psw = password
        self.login_attempts = login_attempts
        
    def describe_user(self):
        print(f'First name: {self.f_name}')
        print(f'Last name: {self.l_name}')
        print(f'Password: {self.psw}')
    
    def greet_user(self):
        full_name = self.f_name + self.l_name
        print(f'Hello {full_name}, welcome back... Please enter password to continue.')
        
    def increment_login_attempts(self):
        ...
        
    def reset_login_attempts(self):
        ...
        
user1 = users('Monkey D ', 'Luffy', 'Meat')
user2 = users('Roranoa ', 'Zoro', 'Three sword style')

print(user1.greet_user())
print(user1.describe_user())
print(user1.greet_user())
print(user2.describe_user())