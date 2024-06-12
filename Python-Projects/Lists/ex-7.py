#  Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list. 
# • Print the message Three items from the middle of the list are:. Then use a
# slice to print three items from the middle of the list.
# • Print the message The last three items in the list are:. Then use a slice to
# print the last three items in the list.

invitation = ['Jesus Christ', 'Mom', 'Dad', 'Sister', 'Grandma', 'Relative1', 'Relative2', 'Relative3']
print(f'The first three items in the list are: {invitation[:3]}')
print(f'Three items from the middle of the list are: {invitation[4]}')
print(f'The last three items in the list are: {invitation[-3:]}')

print('\n')

# My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the
# following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite pizzas are:, 
# and then use a for loop to print the first list. Print the message My
# friend’s favorite pizzas are:, and then use a for loop to print the second list.
# Make sure each new pizza is stored in the appropriate list.


pizzas = ['pepperoni pizza', 'chicken pizza', 'veg pizza']
friend_pizzas = pizzas[:]
print(friend_pizzas)

pizzas.append('egg pizza')
print(pizzas)

friend_pizzas.append('biriyani pizza')
print(friend_pizzas)
print('\n')

for pizza in pizzas:
    print(f'My favorite pizzas are: {pizza}')
    
print('\n')

for f_pizza in friend_pizzas:
    print(f'My favorite pizzas are: {f_pizza}')
    
print('\n')

# More Loops: All versions of foods.py in this section have avoided using
# for loops when printing, to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods

food = ['Biryani', 'Mandhi', 'Mutton', 'Chicken0', 'Beaf']
print("List of foods:")
for item in food:
    print(item)
