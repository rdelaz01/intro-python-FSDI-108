# Sets are used to store multiple items in a single variable 
# sets are Unordered, UNindexed, and have no Duplicates

# sets are written with {}

fruits = {"apple", "banana", "cherry"}
print(fruits) 

# No duplicates allowed 
fruits = {"apple", "banana", "apple"}
print(fruits) # ignores duplicates and does  not show error

# check if item exist 
print("banana" in fruits)

# adding items 
fruits.add("orange")
print(fruits)

#adding Multiple items
fruits.update(["kiwi","mango"])
print(fruits)

#removing items
fruits.remove("banana")
print(fruits)

fruits.discard("water") #discard function removes items without errors incase of non existance 
print(fruits)

# Set operations (like math)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2)) #union combines both sets / no duplicates
print(set1.intersection(set2)) # only returning common elements or duplicates
print(set1.difference(set2)) # shows only whats in set 1 

"""
MINI CHALLENGE
"""

invited_friends = {"Alex", "Sam", "Leo", "Nina"}
rsvped = {"Nina", "Sam", "jordan"}
print(invited_friends.union(rsvped))
print(rsvped)
print(invited_friends.difference(rsvped))

invited_friends.update(["tom", "jerry"])
print(invited_friends)

rsvped.discard("Leo")
print(rsvped)
print(len(rsvped))

if "Leo" in rsvped:
    print("Leo is coming")
else: print("Leo is not coming")







