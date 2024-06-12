# Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includeet of invitation mes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

invitation = ['Jesus Christ', 'Mom', 'Dad', 'Sister', 'Grandma', 'Relative1', 'Relative2', 'Relative3']
print(f'Hey {invitation[0]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[1]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[2]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[3]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[4]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[5]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[6]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[7]} im making some tasty dinner tonight would u like to join.')

print('\n')

# Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of
# your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the
# name of the new person you are inviting.
# • Print a second set of  invitation message, one for each person who is still in
# your list.

guest_who_cant_make_it = invitation[-1]
print(f'{guest_who_cant_make_it} cant make it to the dinner.')
print('\n')

# so removing that element and adding a new one
modified_invitation = invitation.pop()
invitation.append('Neighbour1')

print(f'Hey {invitation[0]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[1]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[2]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[3]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[4]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[5]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[6]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[7]} im making some tasty dinner tonight would u like to join.')

print('\n')

# More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
# end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

invitation.append('Neighbour2')
invitation.append('Friend1')
invitation.append('Friend2')

print(f'Hey {invitation[1]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[2]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[3]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[4]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[5]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[6]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[7]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[8]} im making some tasty dinner tonight also i found a bigger table would u like to join.')
print(f'Hey {invitation[9]} im making some tasty dinner tonight also i found a bigger table would u like to join.')
print(f'Hey {invitation[10]} im making some tasty dinner tonight also i found a bigger table would u like to join.')

print('\n')

invitation.insert(0, 'God')
invitation.insert(6, 'Enemy')
invitation.append('Stranger')

print(f'Hey {invitation[0]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[1]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[2]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[3]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[4]} im making some tasty dinner tonight would u li your list, ke to join.')
print(f'Hey {invitation[5]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[6]} im making some tasty dinner tonight also i found a bigger table would u like to join.')
print(f'Hey {invitation[7]} im making some tasty dinner tonight would u like to join.')
print(f'Hey {invitation[8]} im making some tasty dinner tonight also i found a bigger table would u like to join.')
print(f'Hey {invitation[9]} im making some tasty dinner tonight also i found a bigger table would u like to join.')
print(f'Hey {invitation[10]} im making some tasty dinner tonight also i found a bigger table would u like to join.')
print(f'Hey {invitation[11]} im making some tasty dinner tonight also i found a bigger table would u like to join.')
print(f'Hey {invitation[12]} im making some tasty dinner tonight also i found a bigger table would u like to join.')
print(f'Hey {invitation[13]} im making some tasty dinner tonight also i found a bigger table would u like to join.')

print('\n')

# Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and now you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from print a
# message to that person letting them know you’re sorry you can’t invite them
# to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end of
# your program.

print('Oops You can invite only two people')
print(f'Sorry {invitation[-1]} something came up so i cant invite you... lets catch up some other time.')
invitation.pop()
print(f'Sorry {invitation[-1]} something came up so i cant invite you... lets catch up some other time.')
invitation.pop()
print(f'Sorry {invitation[-1]} something came up so i cant invite you... lets catch up some other time.')
invitation.pop()
print(f'Sorry {invitation[-1]} something came up so i cant invite you... lets catch up some other time.')
invitation.pop()
print(f'Sorry {invitation[-1]} something came up so i cant invite you... lets catch up some other time.')
invitation.pop()
print(f'Sorry {invitation[-1]} something came up so i cant invite you... lets catch up some other time.')
invitation.pop()
print(f'Sorry {invitation[-1]} something came up so i cant invite you... lets catch up some other time.')
invitation.pop()
print(f'Sorry {invitation[-1]} something came up so i cant invite you... lets catch up some other time.')
invitation.pop()
print(f'Sorry {invitation[-1]} something came up so i cant invite you... lets catch up some other time.')
invitation.pop()
print(f'Sorry {invitation[-1]} something came up so i cant invite you... lets catch up some other time.')
invitation.pop()
print(f'Sorry {invitation[-1]} something came up so i cant invite you... lets catch up some other time.')
invitation.pop()
print(f'Sorry {invitation[-1]} something came up so i cant invite you... lets catch up some other time.')
invitation.pop()

print('\n')

print(f'Hey {invitation[0]} you are still invited to the dinner i hope you make...')
print(f'Hey {invitation[1]} you are still invited to the dinner i hope you make...')

print('\n')

del invitation[0]
del invitation[0]

print(f'{invitation} List is Empty')

print('\n')

# Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (pages 41–42), use len() to print a message indicating the number
# of people you’re inviting to dinner

print(f'Number of people invited: {len(invitation)}')