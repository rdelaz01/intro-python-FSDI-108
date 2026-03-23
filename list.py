# Lists are used to dtore multiple items in a single variable
# Think of a containter that can hold multiple items, like a box or a bag
# lists are written with square brackets [] and the items are separated by commas

my_list = [10, 20, 30, 40, 50]
print(my_list) # prints the entire list

# list can contail different data types
mixed_list = [1, "apple", 3.5, True]
print(mixed_list) # prints the entire list

#you can acces list item by using the index (position) of the item in the list
#(indexing start at 0)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0]) # prints "apple"
print (fruits[4]) # prints "elderberry"

# you can also use a NEGATIVE indexes to count from the end 
print(fruits[-1]) # prints "elderberry"

#modify list items
fruits[1] = "blueberry" # change "banana" to "blueberry"
print(fruits) # prints the modified list

#adding items to a list
fruits.append("orange") # adds "orange" to the end of the list
print(fruits) # prints the modified list

fruits.insert(1, "grape") # inserts "grape" at index 1
print(fruits) # prints the modified list

#removing items from a list
fruits.remove("date") # removes "date" from the list
print(fruits) # prints the modified list

fruits.pop() # removes the last item from the list
print(fruits) # prints the modified list

#looping through a list
for fruit in fruits:
    print(fruit) # prints each fruit in the list on a new line

#check if item exist in a list

if "apple" in fruits:
    print("apple is in the list") # prints "apple is in the list"

# list length 
print(len(fruits)) # prints the number of items in the list

"""
ASSIGNMENT 2
"""
#creat list
top_anime = ["Naruto", "One Piece", "Attack on Titan", "My Hero Academia", "Demon Slayer"]
print(top_anime)

#access items by index
print(top_anime[0])

#replace item
top_anime[1] = "Dragon Ball Z"
print(top_anime)

#removing item by index

top_anime.remove("My Hero Academia")
print(top_anime)

#print list length
print(len(top_anime))

