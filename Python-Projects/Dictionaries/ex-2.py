# . Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.

glossary = {'list': 'list is a collection of elemensts', 'tuple': 'It is just like list but immutable', 'variables': 'it is like a container that holds values', 'loops': 'helps to iterate over something which helps to execute again and again until certain condition is met', 'if': 'it is a condition that helps to make choices'}
for key, value in glossary.items():
    print(f'{key}:')
    print('   ',value)
    
print('\n')    

# Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary

rivers = {'nile': 'egypt', 'red sea': 'somewhere'}
for riv, val in rivers.items():
    print(f'The {riv} runs through {val}')
    
print('\n')    

# Polling: Use the code in favorite_languages.py (page 96).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people_to_poll = ['jen', 'sarah', 'edward', 'phil', 'michael', 'alice', 'bob']

for people in people_to_poll:
    if people in favorite_languages:
        print(f'Thank you {people} for responding')
    else:
        print(f'hello {people} im inviting you to take the poll, Kindly fill the details.')