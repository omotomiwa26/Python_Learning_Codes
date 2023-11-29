#----------Extract First Names------------#
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)

#-------------Multiples Of Three---------#
multiples_of_3 = [x*1 for x in range(3, 61, 3)] 
print(multiples_of_3)