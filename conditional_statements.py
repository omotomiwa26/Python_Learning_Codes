#----------Bank banlace--------------#
phone_balance = 5
bank_balance = 50

if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance)
print(bank_balance)


#---------------Even or Odd numner check--------------#
number = 14
if number % 2 == 0:
    print("Number " +str(number) + " is even." )
else:
    print("Number " + str(number) + " is odd. ")


#----------------Ticket Price-----------------#
age = 64

free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

concession_ticket = 1.25
adult_ticket = 2.50

if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket
print("Somebody who is {} years old will pay ${} to ride the bus".format(age, ticket_price))

#-------------points and prize--------------#
points = 100  # use this input to make your submission

prize1 = "wooden rabbit"
prize3 = "wafer-thin mint"
prize4 = "penguin"

# write your if statement here
if (points >=1 and points <=50):
    result = F"Congratulations! You won a {prize1}!"
elif (points >=51 and points <=150):
    result = "Oh dear, no prize this time."
elif (points >=15 and points <=180):
    result = F"Congratulations! You won a {prize3}!"
elif (points >=181 and points <=120):
    result = F"Congratulations! You won a {prize4}!"
else:
    result = "Points not valid"

print(result)