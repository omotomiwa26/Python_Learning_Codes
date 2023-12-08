#-------------------population density function--------------#
# write your function here
def population_density(population, land_area):
    total_population = population / land_area
    return total_population

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

#-----------readable timedelta------------------------#
# write your function here
def readable_timedelta(days):
    nos_of_weeks = days // 7
    nos_of_days = days % 7
    return F"{nos_of_weeks} week(s) and {nos_of_days} day(s)."

# test your function
print(readable_timedelta(5094))