elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
print(elements['helium'])
elements['lithium'] = 3
print('carbon' in elements)
print(elements.get('dilithium'))

n = elements.get('dilithium')
print(n is None)
print(n is not None)

