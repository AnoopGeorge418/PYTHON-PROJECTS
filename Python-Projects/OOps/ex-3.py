#  Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote in
# Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
# will work; just pick the one you like better. Add an attribute called flavors that
# stores a list of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
        
    def describe_restaurant(self):
        print(f'Name of the Restaurant: {self.restaurant}')
        print(f'Cuisine type: {self.cuisine}')
        
    def open_restaurant(self):
        return 'Restaurant is Open.'

print('\n')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['Venila', 'Choclate', 'Chikku', 'Badaam', 'Nuts', 'Grapes', 'Mango']
        
    def display_flavours(self):
        print(self.flavours)
        
ice_cream_stand = IceCreamStand('The great kitchen', 'Worldly')
ice_cream_stand.display_flavours()

print('\n')

# Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
# strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method

class users:
    def __init__(self, first_name, last_name, password):
        self.f_name = first_name
        self.l_name = last_name
        self.psw = password
        self.login_attempts = 0
        
    def describe_user(self):
        print(f'First name: {self.f_name}')
        print(f'Last name: {self.l_name}')
        print(f'Password: {self.psw}')
    
    def greet_user(self):
        full_name = self.f_name + self.l_name
        print(f'Hello {full_name}, welcome back... Please enter password to continue.')
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        

class Admin(users):
    def __init__(self, first_name, last_name, password):
        super().__init__(first_name, last_name, password)
        self.privileges = ['can add post', "can delete post", "can ban user"]
        
    def show_privileges(self):
        print(self.privileges)
        
admin = Admin('Anoop', 'George', '1234')
admin.show_privileges()

print('\n')

# Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.

class Privileges:
    def __init__(self, privileges = []):
        self.privileges = privileges
        
    def show_privileges(self):
        print('Privileges: ')
        for priv in self.privileges:
            print(priv)

class Admin(users):
    def __init__(self, first_name, last_name, password):
        super().__init__(first_name, last_name, password)
        self.privileges = Privileges(['can add post', 'can delete post', 'can ban user'])
        
        
admin = Admin('Anoop', 'George', '1234')
admin.privileges.show_privileges()