# Stripping Whitepsace
s = '   This is a sentence with whitespace.       \n'
print(f'Strip leading whitespace: {s.lstrip()}')
print(f'Strip trailing whitespace: {s.rstrip()}')
print(f'Strip all whitespace: {s.strip()}')

'''
output:
Strip leading whitespace: This is a sentence with whitespace.       

Strip trailing whitespace:    This is a sentence with whitespace.
Strip all whitespace: This is a sentence with whitespace.
'''
s = 'This is a sentence with unwanted characters.AAAAAAAA'
print(f"Strip unwanted characters: {s.rstrip('A')}") 

'''
output:
Strip unwanted characters: This is a sentence with unwanted characters.
'''

# Splitting Strings

s = 'KDnuggets is a fantastic resource'
print(s.split())

s = 'these,words,are,separated,by,comma'
print('\',\' separated split -> {}'.format(s.split(',')))

s = 'abacbdebfgbhhgbabddba'
print('\'b\' separated split -> {}'.format(s.split('b')))

'''
output:
['KDnuggets', 'is', 'a', 'fantastic', 'resource']
',' separated split -> ['these', 'words', 'are', 'separated', 'by', 'comma']
'b' separated split -> ['a', 'ac', 'de', 'fg', 'hhg', 'a', 'dd', 'a']
'''

# Joining List Elements Into a String
s = ['KDnuggets', 'is', 'a', 'fantastic', 'resource']
print(' '.join(s))

'''
output:
KDnuggets is a fantastic resource
'''

s = ['Eleven', 'Mike', 'Dustin', 'Lucas', 'Will']
print(' and '.join(s))
'''
output:
Eleven and Mike and Dustin and Lucas and Will
'''

# Reversing a String
s = 'KDnuggets'
print(f'The reverse of KDnuggets is: {s[::-1]}')
'''
output:
The reverse of KDnuggets is: steggunDK
'''

# Replacing Substrings
s1 = 'The theory of data science is of the utmost importance.'
s2 = 'practice'
print(f"The new sentence: {s1.replace('theory', s2)}")
'''
output:
The new sentence: The practice of data science is of the utmost importance.
'''

# Combining the Output of Multiple Lists

countries = ['USA', 'Canada', 'UK', 'Australia']
cities = ['Washington', 'Ottawa', 'London', 'Canberra']

for x, y in zip(countries, cities):
  print(f'The capital of {x} is {y}.')

'''
output:
The capital of USA is Washington.
The capital of Canada is Ottawa.
The capital of UK is London.
The capital of Australia is Canberra.
'''