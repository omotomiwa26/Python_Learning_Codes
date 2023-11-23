book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

book_dict = {}

for word in book_title:
    if word not in book_dict:
        book_dict[word] = 1
    else:
        book_dict[word] += 1
print(book_dict)
