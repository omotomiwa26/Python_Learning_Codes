#----------Extract First Names------------#
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)

#-------------Multiples Of Three---------#
multiples_of_3 = [x*1 for x in range(3, 61, 3)] 
print(multiples_of_3)

#--------------Filter Names By Scores---------------#
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)