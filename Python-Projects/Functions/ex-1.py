#  Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.

def favorite_book(title):
    print(f'One of my favorite book: {title}')
    
favorite_book('Alice in wonderland')

print('\n')

# T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print a
# sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

def make_shirt(size, text):
    print(f'{size} and {text} for the shirt will be printed on it')
    
make_shirt(21, 'Learn Every time')
make_shirt(size = 21, text = 'Do great things')

print('\n')

#  Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size = 'Large', text = 'I love Python'):
    print(f'{size} and {text} for the shirt will be printed on it')

make_shirt()
make_shirt('Medium', 'I love to learn')
make_shirt(size='Small', text='Python is awesome!')

print('\n')

# Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.

def describe_city(city, country = 'India'):
    print(f'{city} is in {country}')
    
describe_city('Mangalore')
describe_city('Bangalore')
describe_city('New york', country = 'United states')
