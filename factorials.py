#-----------for loop factorial----------#
# number to find the factorial of
number = 6 
# start with our product equal to one
product = 1
# write your for loop here
for n in range(1, number+1):
    product *= n
# print the factorial of number
print(product)

#---------while loop factorail-------------#
# number to find the factorial of
number = 5   
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1
# write your while loop here
while number >= current:
    #multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1
# print the factorial of number
print(product)