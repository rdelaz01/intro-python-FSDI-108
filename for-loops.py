"""
A loop for Python is a control structure that lets you repeat a block of code for each item 
in a sequence (such as lis, strings, tuples, range of numbers etc..)

'for' variable in sequence:
    #Code block runs for each item in the sequence 
"""
#Basic example
fruits = ["apples", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


for letter in "Rollie":
    print(letter)

print("___________________________________________________")

# range() generates a sequence of numbers 
for x in range(5): #
    print(x)

print("_______________________________________________________")
#start and end range 
for x in range(2,6):
    print(x)


print("_____________________________________")
#step

for x in range(0, 10, 2):
    print(x)


"""
MINI CHALLENGE
"""

num = int(input("Enter number!"))

for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")