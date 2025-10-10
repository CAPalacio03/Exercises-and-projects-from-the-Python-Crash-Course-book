"""
 Make a list of the numbers from one to one million, 
and then use min() and max() to make sure your list actually starts at one and 
ends at one million. Also, use the sum() function to see how quickly Python can 
add a million numbers.
"""

# Creat a list of numbers
numbers = list(range(1,1000001))

print('The list stars in: ', min(numbers))

print('The list ends in: ', max(numbers))

print('The sum of the list is: ', sum(numbers))