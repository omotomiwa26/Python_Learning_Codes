my_string = 'sebastian thrum'
my_string.islower()
my_string.count('a')
my_string.find('a')

print('Mohamed has {} ballons'.format(27))

animal = 'dog' 
action = 'bite'
print('Does your {} {}?'.format(animal, action))

maria_string = 'Maria loves {} and {}'
print(maria_string.format('math', 'statistics'))


str = 'The cow jumped over the moon.'
new_str = str.split()
print(new_str)
new_str = str.split(' ', 3)
print(new_str)
new_str = str.split('.')
print(new_str)
new_str = str.split(None, 3)
print(new_str)