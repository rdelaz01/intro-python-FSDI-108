print("Hello World From Python!") # No semicolon needed 
print(2) # Prints the integer 2
print(5+3) # Prints the result of 5 plus 3 (8)
print(True) # Prints the boolean value True

#Shortcuts 
#CTRL + / to comment out a line of code
#how to run last command in terminal: up arrow key

# comment test
#asdfasdf
"""
comment test
asdfasdf    
yolo
"""

# Variables and Concatenation

name = "john"
age = 30
print(name) # Prints the value of the variable name (john)

# Concatenation is joining two strings together with a plus sign (+)
print("My name is "+ name + " and I am " + str(age) + " years old") # convert int to string with str() function

name = "john"
age = 7
middle_name = "Dispo"
last_name = "Delacruz"
found = False

print("My name is " + name + " " + middle_name + " " + last_name + " and I am " + str(age) + " years old")
print("did he show up to class?" + str(found)) # convert boolean to string with str() function

#mini challenge: 
"""
write a short story  and initialize varieables (stings and numbers)
Use print() and concatenate the variables to tell the story
Run the code in the terminal to see the output
"""

name = "gojo"
last_name = "satoru"
power = "limitless"
student = "yuji"
foe = "sukuna"
print("Once upon a time, there was a powerful sorcerer named " + name + " " + last_name + ".")
print("He had a special power called " + power + ".")
print("One day, he took on a student named " + student + " to teach him how to control his power.")
print("However, they soon faced a formidable foe named " + foe + ", who threatened to destroy everything they held dear.")
print("Together, " + name + " and " + student + " fought against " + foe + " to protect their world and ensure the safety of their loved ones.")
print("In the end, they emerged victorious, and their bond grew stronger than ever before.")


#F-strings (formatted strings)
# Cleaner way to format strings 

work = "UTS"
job = "MMechanic"
# start with f before the string and use curly braces {} to include variables directly in the string
print(f"I work at {work} as a {job}!") 

#multi line f-string 
print(f"""    
my name is {name} {last_name}.
I like python 
    types   indentation
""")

# type function 
print(type(name)) # prints the type of the variable name (str)
print(type(age)) # prints the type of the variable age (int)
print(type(found)) # prints the type of the variable found (bool)

#casting (changing data types)
print(20+ int("20")) # this will cause an error because "age" is a string and cannot be converted to an integer.
print(20+ age ) # adding an integer and an integer results in an integer (50)
print(20+ 2.98) # adding an integer and a float results in a float (22.98)

#user input
#input() lets the user enter data type values into the terminal 

user_name = input("Enter your name: ")
print(f"Hello, {user_name}!") # display user input using f-string

print(input("Enter your age: ")) # this will print the age entered by the user, but it will be treated as a string

#EXAMPLE 1: converting input to an integer
new_age = int(input("Enter your age: ")) # convert the input to an integer
print(age + new_age) # this will add the user's age to the existing age variable and print the result

# Mini challege 
"""
Pizza Calculator
    - Ask how many silces of pizza and how many people
    - Use math operation to calculate slices per person 
    - show the results with an f-string
"""
slices = int(input("How many slices of pizza?"))
people = int(input("How many people?"))
print(f"{slices} / {people} = {slices / people} slices per person")