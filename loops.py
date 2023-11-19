#-------------quick brown fox------------#
lists = ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']

for list in lists:
    print(list)

#------------nultiple of 5-----------------#
for num in range(5, 31, 5):
    print(num)

#-------------create usernames-----------#
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for index in range(len(names)):
    names[index] = names[index].lower()
    usernames.append(names[index].replace(" ", "_"))
print(usernames)

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(" ", "_")
print(usernames)

#------------Tag Counter----------#
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count +=1
print(count)

#---------------create HTML list--------------#
items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line
for index in range(len(items)):
    html_str += F'<li>{items[index]}</li>\n'
html_str += '</ul>'

print(html_str)