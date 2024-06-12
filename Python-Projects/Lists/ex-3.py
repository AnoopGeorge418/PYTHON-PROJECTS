# Think of at least five places in the world you’d like
# to visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly;
# just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed

locations = ['heaven', 'israel', 'usa', 'mount everest', 'japan']

print(f'Original Order: {locations}')
print(f'Sorted in Alphabetical: {sorted(locations)}')
print(f'Original Order: {locations}')
print(f'Reversed using sorted: {sorted(locations, reverse=True)}')
print(f'Original Order: {locations}')
locations.reverse()
print(f'Reversed Order: {locations}')
locations.reverse()
print(f'Original Order restored: {locations}')
locations.sort()
print(f'Permanent Change to Alphabetical Order: {locations}')
locations.sort(reverse=True)
print(f'Permanent Change to Reverse Alphabetical Order: {locations}')

print('\n')

# Every Function: Think of things you could store in a list. For example, you
# could make a list of mountains, rivers, countries, cities, languages, or anything
# else you’d like. Write a program that creates a list containing these items and
# then uses each function introduced in this chapter at least once.

list_of_all_things = ['mount everest', 'red sea', 'india', 'usa', 'mangalore', 'bangalore', 'kannada', 'tamil', 'english']
# appending
list_of_all_things.append('japan')
print(list_of_all_things)
# inserting
list_of_all_things.insert(0, 'God')
print(list_of_all_things)
# pop
list_of_all_things.pop()
print(list_of_all_things)
# pop by index
list_of_all_things.pop(0)
print(list_of_all_things)
# del 
del list_of_all_things[0]
print(list_of_all_things)
# remove
list_of_all_things.remove('kannada')
print(list_of_all_things)
# sorted
print(sorted(list_of_all_things))
# reverse sorted
print(sorted(list_of_all_things, reverse=True))
print(list_of_all_things)
# reverse
list_of_all_things.reverse()
print(list_of_all_things)
# sort
list_of_all_things.sort()
print(list_of_all_things)
# sort reverse
list_of_all_things.sort(reverse=True)
print(list_of_all_things)
# len
print(len(list_of_all_things))
# removing entire items in list
del list_of_all_things