elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
print(elements['helium'])
elements['lithium'] = 3
print('carbon' in elements)
print(elements.get('dilithium'))

n = elements.get('dilithium')
print(n is None)
print(n is not None)

# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}

elements = {
    'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
    'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}
    }

#helium = elements['helium']
#hydrogen_weight = elements = elements['hydrogen']['weight']

oxygen = {'number': 8, 'weight': 15.999, 'symbol': 'O'}
elements['oxygen'] = oxygen
print('elements = ', elements)

elements = {
    'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
    'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}
}

