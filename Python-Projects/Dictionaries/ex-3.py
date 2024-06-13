#  People: Start with the program you wrote for Exercise 6-1 (page 98). Make
# two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through
# the list, print everything you know about each person.

persons1 = {'Luffy': 'captain', 'zoro': 'vicecaptain', 'sanji': 'cook', 'ussop': 'sniper', 'nami': 'navigator'}
persons2 = {'chopper': 'doctor', 'jimbei': 'henchman', 'franky': 'shipwright', 'robin': 'archaelogist'}
persons3 = {'shanks': 'haki beast', 'dragon': 'unknown', 'sabo': 'bro in arms', 'ace': 'bro in arms', 'kaido': 'Strongest creature'}

Persons = [persons1, persons2, persons3]
for people in Persons:
    print(people)
    
print('\n')

# Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet

pet1 = {'owner': 'luffy', 'animal': 'dragon'}
pet2 = {'owner': 'zoro', 'animal': 'tiger'}
pet3 = {'owner': 'sanji', 'animal': 'fish'}
pets = [pet1, pet2, pet3]
for pet in pets:
    print(pet)
    
print('\n')

# Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places for
# each person. To make this exercise a bit more interesting, ask some friends to
# name a few of their favorite places. Loop through the dictionary, and print each
# person’s name and their favorite places.

places = {'luffy': ['egghead', 'eastblue', 'west blue'], 'zoro': ['egghead', 'eastblue', 'west blue']}
for key, values in places.items():
    print(key, values)
    
    
print('\n')

favorite_numbers = {
    'Alice': [5, 12, 7],
    'Bob': [7, 22, 30],
    'Charlie': [9, 16, 25]
}

# Looping through the dictionary and printing each person's favorite numbers
for person, numbers in favorite_numbers.items():
    print(f"\n{person}'s favorite numbers:")
    for number in numbers:
        print(f"- {number}")