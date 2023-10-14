months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(months[0])
print(months[7])
print(months[-2])
print(months[10])
print(len(months))

print(months[6:9])
print(months[:6])
print(months[6:])

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
num_days = days_in_month[9]

print(num_days)