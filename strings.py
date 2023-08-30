# TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
print (ford_quote)


## string quiz 2
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name + ' ') + len(middle_names + ' ') + len(family_name)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)