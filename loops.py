#-------------quick brown fox------------#
lists = ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']

for list in lists:
    print(list)

#------------nultiple of 5-----------------#
for num in range(5, 31, 5):
    print(num)

#-------------name range-----------#
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for index in range(len(names)):
    names[index] = names[index].lower()
    usernames.append(names[index].replace(" ", "_"))
print(usernames)