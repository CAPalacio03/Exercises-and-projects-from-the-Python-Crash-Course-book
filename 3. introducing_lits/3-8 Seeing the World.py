"""
Think of at least five places in the world ypu'd like to visit
"""

# Store the locations in a list. Make sure the list is not alphabetical order.
locations = ['Dublin', 'Londres', 'Zurich', 'Seul', 'El Cairo', 'Machu Pichu']

# Print your list in its original order. 
print(locations)

# Use sorted() to print your list in alphabetical order without modifiying the actual list.
print(sorted(locations))

# Show that your list is still in its original order.
print(locations)

# Use sorted() to print your list in reverse alphabetical order 
# without changeing the order of the origonal order 
print(sorted(locations, reverse=True))

# Show that your list is still in its original order by priting it again
print(locations)

# Use reverse() to change the order of your list. 
locations.reverse()

# Print the list to show it's back to its original order.
print(locations)

# Use reverse() to change the order of your list again.
locations.reverse()

# Print the list to show it's back to  its original oreder.
print(locations)

# Use sort() to change your list so it's stored un alphabetical order.
locations.sort()

# Print the list to show that its order has benn changed
print(locations)

# Use sort() to change your list so it's stored in reverse alphabetical order.
locations.sort(reverse=True)

# Print the lsit to show that its order has changed
print(locations)