# Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping, print
# a message saying you’ll add that topping to their pizza.

while True:
    user = input('Toppings: ').lower()
    if user == 'q':
        break
    else:
        print("You’ll add that topping to their pizza.")

print('\n')

# Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
# each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

active = True
while active:
    user = input('Toppings: ').lower()
    if user == 'q':
        active = False