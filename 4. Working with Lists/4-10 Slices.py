"""
Using one of the programs you wrote in this chapter, add several 
lines to the end of the program that do the following:
"""

numbers = list(range(1,1000001))

# Print the message The first three items in the list are:
print('The frist three itms in the list are:')
print(numbers[:3])

# Print the message Three items from the middle of the list are:
print('Three items form the middle of the list are:')
middle = int(len(numbers)/2)
print(numbers[middle-2:middle+1])

# Print the message The last three items in the list are:
print('The last three items in the list are:')
print(numbers[-3:])