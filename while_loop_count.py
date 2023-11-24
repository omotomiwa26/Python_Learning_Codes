#-----------while count----------------#
start_num = 5
end_num = 100
count_by = 2

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
break_num = start_num
while break_num <= end_num:
    break_num += count_by
print(break_num)

#-----------------if while count----------#
start_num = 500
end_num = 100
count_by = 2 
# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
if end_num <= start_num:
    result = F"Oops! Looks like your start value is greater than the end value. Please try again."
else:
    break_num = start_num
    while break_num <= end_num:
        break_num += count_by
    result = break_num

print(result)

#---------------nearest square------------#
limit = 40

n = 0
while (n+1)**2 < limit:
    n+=1
    nearest_square = n**2
    print(nearest_square)
#------------while odd count---------------#
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
ind = 0

while (count_odd < 5) and (ind < len(num_list)): 
    if num_list[ind] % 2 != 0:
        list_sum += num_list[ind]
        count_odd += 1
    ind += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))