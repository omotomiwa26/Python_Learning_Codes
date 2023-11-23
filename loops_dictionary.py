book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

book_dict = {}

for word in book_title:
    if word not in book_dict:
        book_dict[word] = 1
    else:
        book_dict[word] += 1
print(book_dict)


#---------------------------------#
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
for keys, values in cast.items():
    print(F"Actor{keys}    Role{values}")


#------------dictionary fruit count------------#
fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary

#if the key is in the list of fruits, add to fruit_count.
for keys,values in basket_items.items():
    if keys in fruits:
        fruit_count += values

#if the key is not in the list, then add to the not_fruit_count
for keys,values in basket_items.items():
    if keys not in fruits:
        not_fruit_count += values



print(fruit_count, not_fruit_count)