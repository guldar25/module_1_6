my_dict = {"name" : "Guldar" , "year_of_birth" : 2002}
print(my_dict["name"])
my_dict["surname"] = "Yasybaeva"
my_dict.update({"Sasha" : 2001 , "Lola" : 2000})
print(my_dict)
a = my_dict.pop("surname")
print(my_dict)
print(a)

my_set = {1, "name", 3, 1, True, 3.1, 3, False, "name"}
print(my_set)
print(my_set.add(6))
print(my_set.add("ufa"))
print(my_set)