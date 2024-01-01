#--------------lambda with map---------------#
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

averages2 = list(map(lambda num: sum(num) / len(num), numbers))
print (averages2)


#------------lambda with filter---------------#
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)

short_cities2 = list(filter(lambda city: len(city) < 10, cities))
print(short_cities2)