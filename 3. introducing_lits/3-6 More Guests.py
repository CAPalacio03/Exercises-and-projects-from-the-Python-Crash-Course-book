"""
You just found a bigger dinner table, so now more space is available. 
Think of three more guests to invite to dinner.
"""
# Start with your program from  Exercise 3-5. 
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
print(f'Dear {guests[5]}, I would like to invite you to dinner to night')
