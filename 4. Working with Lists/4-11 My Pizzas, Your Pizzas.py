"""
Start with your program from Exercise 4-1 
(page 56). Make a copy of the list of pizzas, and call it friend_pizzas. 
Then, do the following:
"""

pizzas = ['Perperoni', 'Mix', 'Mexican']

#  Make a copy of the list of pizzas
friend_pizzas = pizzas[:]

# Add a new pizza to the original list.
pizzas.append('Margherit')

# Add a different pizza to the list friend_pizzas.
friend_pizzas.append('Hawaiian')

# Prove that you have two separate lists
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('\nMy friend’s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)