my_string = 'sebastian thrum'
print(my_string.islower())
print(my_string.count('a'))
print(my_string.find('a'))

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

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
print(len(verse))
print(verse.find('and'))
print(verse.rfind('you'))
print(verse.count('you'))