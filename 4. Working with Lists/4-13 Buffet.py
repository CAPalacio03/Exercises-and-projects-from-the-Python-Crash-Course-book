"""
Buffet: A buffet-style restaurant offers only five basic foods. Think of five 
simple foods, and store them in a tuple.
"""

foods = ('Soup', 'Hamburger', 'Pizza', 'Salad', 'Ice Cream')

# Use a for loop to print each food the restaurant offers.
for food in foods:
    print(food)

# Try to modify one of the items
try:
    foods[2] = 'steak'
except TypeError as e:
    print(e)

# replacing two of the items with different foods
foods = ('Soup', 'Hamburger', 'Steal', 'Salad', 'Ice Creama')

for food in foods:
    print(food)