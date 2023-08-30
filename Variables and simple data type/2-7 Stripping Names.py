'''
Use a variable to represent a person’s name, and include some whitespace characters at 
the beginning and end of the name. Make sure you use each character combination, 
"\t" and "\n", at least once. Print the name once, so the whitespace around the name 
is displayed. Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().
'''

name =  '\tCarlos  Alberto\n'

print(f'Name with space: {name}')
print(f'Name with rstrip funtion: {name.rstrip()}')
print(f'Name with lstrip funtion: {name.lstrip()}')
print(f'Name with strip funtion: {name.strip()}')



