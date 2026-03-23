#Tuples are just like list - they can store multiple items but cant be changed 
# They are IMMUTABLE(cant be changed after creation)

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

#accessing items
print(my_tuple[0])
print(my_tuple[2])

#check if item exist 

if "apple" in my_tuple:
    print("yes, apple is in tuple")

#length of a tuple

print(len(my_tuple))

#single item tuple
#you MUST add a comma at the end or python wont recognize it as a tuple 

single = ("grape")
print(type(single))
tuple = ("water",)
print(type(tuple))

#Nested Tuples
tuple1 = ("a", "b", "c")
tuple2 = (1,2,3)
combine = (tuple1, tuple2)
print(combine)

"""
MINI CHALLANGE
"""

travel_bag =("wallet", "shoes", "passport", "Powerbank", "snacks")
print(travel_bag[1], travel_bag[3])

if "shoes" in travel_bag:
    print("Youre ready to walk")
else: ("You forgot you shoes")

essentials= ("toiletries", "charger", "switch")
final_bag = travel_bag + essentials
print(len(final_bag))
print(final_bag[-1])

