#----------break the string-------------#
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for word in headlines:
    news_ticker += word + ''
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)
#----------prime number check----------#
## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]
# iterate through the check_prime list
for num in check_prime:

## search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):

## number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break

## otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num -1:    
            print("{} IS a prime number".format(num))

