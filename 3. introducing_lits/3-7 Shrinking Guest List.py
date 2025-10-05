""" 
You just found out that your new dinner table won’t 
arrive in time for the dinner, and you have space for only two guests.
"""

# Start with your program from Exercise 3-6
guests = ['Sabrina Carpenter', 'Elizabeth Woolridge', 'Olivia Rodirgo']

print(f'Dear {guests[0]}, I would like to invite you to dinner to night')
print(f'Dear {guests[1]}, I would like to invite you to dinner to night')
print(f'Dear {guests[2]}, I would like to invite you to dinner to nigh\n')

# Add a print() call at the end of your program stating the name the guest who can't make it
print(f"{guests[0]} can't go to dinner\n")

# Modify your list 
# Replacing the name of the guest who can't make it with the name of the new person you ate inviting

guests[0] = 'Lindsey Striling'

# Print a second set of invitation messages, one for each peson who is still in your list
print(f'Dear {guests[0]}, I would like to invite you to dinner to night')
print(f'Dear {guests[1]}, I would like to invite you to dinner to night')
print(f'Dear {guests[2]}, I would like to invite you to dinner to night\n')

# Add a print() call to the end of your program informing people that you found a bigger dinner table.
print("I've found a table bigger\n")

#Use insert() to add one new guest to the beginning of your list.
guests.insert(0, 'Harry Styles')

#Use insert() to add one new guest to the middle of your list.
guests.insert(2, 'Brandom Flowers')

#Use append() to add one new guest to the end of your list.
guests.append('Paul McCartney')

#Print a new set of invitation messages, one for each person in your list.
print(f'Dear {guests[0]}, I would like to invite you to dinner to night') 
print(f'Dear {guests[1]}, I would like to invite you to dinner to night')
print(f'Dear {guests[2]}, I would like to invite you to dinner to night')
print(f'Dear {guests[3]}, I would like to invite you to dinner to night')
print(f'Dear {guests[4]}, I would like to invite you to dinner to night')
print(f'Dear {guests[5]}, I would like to invite you to dinner to night\n')

# Add a new line that prints a message saying that you can invite only two people for dinner.
print("Sorry, I cant invite two people for dinner\n")

# Use pop() to remove guests from your list one at a time until only two names remain in your list. 
# Each time you pop a name from your list, 
# print a message to that person letting them know you’re sorry you can’t invite them to dinner.

uninvited = guests.pop()
print(f"Sorry {uninvited}, but you can't come to dinner")

uninvited = guests.pop(0)
print(f"Sorry {uninvited}, but you can't come to dinner")

uninvited = guests.pop()
print(f"Sorry {uninvited}, but you can't come to dinner")

uninvited = guests.pop()
print(f"Sorry {uninvited}, but you can't come to dinner\n")

# Print a message to each of the two people still on your list.

print(f"Dear, {guests[0]}, I'll be waiting for you for dinner.")
print(f"Dear, {guests[1]}, I'll be waiting for you for dinner.\n")

# Use del to remove the last two names from your list, so you have an empty list.
del guests[0]
del guests[0]

# Print your list to make sure you actually have an empty list at the end of your program.
print(guests)
