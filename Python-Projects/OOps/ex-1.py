# Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
        
    def describe_restaurant(self):
        print(f'Name of the Restaurant: {self.restaurant}')
        print(f'Cuisine type: {self.cuisine}')
        
    def open_restaurant(self):
        return 'Restaurant is Open.'

# creating instance
restaurant = Restaurant('The Great kitchen', 'Chinese')
# calling attributes
print(f'Name of the Restaurant: {restaurant.restaurant}')
print(f'Cuisine type: {restaurant.cuisine}')
# calling method
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())

print('\n')

# Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance

Restaurant1 = Restaurant('The Indian Kitchen', 'Indian')
Restaurant2 = Restaurant('Ocean Pearl', 'Italic')
Restaurant3 = Restaurant('Royal Palace', 'Japanese')

print(Restaurant1.describe_restaurant())
print(Restaurant2.describe_restaurant())
print(Restaurant3.describe_restaurant())

print("\n")

# Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user

class users:
    def __init__(self, first_name, last_name, password):
        self.f_name = first_name
        self.l_name = last_name
        self.psw = password
        
    def describe_user(self):
        print(f'First name: {self.f_name}')
        print(f'Last name: {self.l_name}')
        print(f'Password: {self.psw}')
    
    def greet_user(self):
        full_name = self.f_name + self.l_name
        print(f'Hello {full_name}, welcome back... Please enter password to continue.')
        
user1 = users('Monkey D ', 'Luffy', 'Meat')
user2 = users('Roranoa ', 'Zoro', 'Three sword style')

print(user1.greet_user())
print(user1.describe_user())
print(user1.greet_user())
print(user2.describe_user())