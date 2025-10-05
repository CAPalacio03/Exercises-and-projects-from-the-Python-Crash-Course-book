"""
You just heard that one of your guests can't make the dinner, so you need to send out a new
set of invitations. You'll have to think of someone else to invite.
"""

# Star with your Program from Excercise 3-4.
guests = ['Sabrina Carpenter', 'Elizabeth Woolridge', 'Olivia Rodirgo']

print(f'Dear {guests[0]}, I would like to invite you to dinner to night')
print(f'Dear {guests[1]}, I would like to invite you to dinner to night')
print(f'Dear {guests[2]}, I would like to invite you to dinner to night')

# Add a print() call at the end of your program stating the name the guest who can't make it
print(f"{guests[0]} can't go to dinner")

# Modify your list 
# Replacing the name of the guest who can't make it with the name of the new person you ate inviting

guests[0] = 'Lindsey Striling'

# Print a second set of invitation messages, one for each peson who is still in your list
print(f'Dear {guests[0]}, I would like to invite you to dinner to night')
print(f'Dear {guests[1]}, I would like to invite you to dinner to night')
print(f'Dear {guests[2]}, I would like to invite you to dinner to night')