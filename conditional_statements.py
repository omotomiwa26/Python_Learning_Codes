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

#----------------Number Guess-----------#
# '''
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 190
guess = 55

if answer > guess:
    result = "Oops!  Your guess was too low."
elif answer < guess:
    result = "Oops!  Your guess was too high."
elif anwser == guess:
    result = "Nice!  Your guess matched the answer!"

print(result)

#---------------Tax purchase---------------#
# '''
# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = "MN"
purchase_amount = 500

if state == "CA":
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "MN":
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == "NY":
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)
