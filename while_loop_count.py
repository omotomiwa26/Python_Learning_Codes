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