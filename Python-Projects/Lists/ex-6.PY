# Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive

for i in range(1, 21):
    print(i)
    
print('\n')

# One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing CTRL-C or by closing the output window.). 

for i in range(1, 1001):
    print(i)
    
print('\n')

# Summing a Million: Make a list of the numbers from one to one million, and
# then use min() and max() to make sure your list actually starts at one and ends
# at one million. Also, use the sum() function to see how quickly Python can add
# a million numbers

n = []
for i in range(1, 10000001):
    n.append(i)
    
print(min(n))
print(max(n))
print(sum(n))

print('\n')

# Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number

for i in range(1, 20, 2):
    print(i)
    
print('\n')

# Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to
# print the numbers in your list.

mul = []
for i in range(3, 30):
    mul.append(i*3)
    
print(mul)

print('\n')

# Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

for i in range(1, 11):
    print(i**3)
    
print('\n')

# Cube Comprehension: Use a list comprehension to generate a list of the first
# 10 cubes.

cube = [cube**3 for cube in range(1, 11)]
print(cube)