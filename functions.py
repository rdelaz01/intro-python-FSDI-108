"""
A function is a block of code that only runs when it is called
We pass data from funtioon (parameter), and the can return data. 

def function_name(parameters):
    # Code Block (indented)
    #Perform actions using the parameters
    return value # optional

"""

#Simple function without parameters

def my_function():
    print("This is my function")# This runs when the function is called 

my_function() # calling the function 

def other__function():
    print("This is another function")

other__function()

#function with parameters 

def print_full_name(first_name, last_name, middle_name):
    print(f"The name is:{first_name}{last_name}{middle_name}")

print_full_name("Rollie" , "Delacruz" , "D")


# Functions That return Values
#Instead of just printing, functions can send back (return) data. 

def get_full_name(fname, lname):
    return f"{fname} {lname}" #Send back the full name as text

#Store the returned value in a variable 
full_name = get_full_name("Rollie", "Delacruz")
print(full_name)

# function with defualt parameters 
# A defualt parameter means the function will use that value-
#if no arguement is provided when calling the  function 

def greet(name="student"):
    print(f"Hello, {name}! Welcome to class")

#Calling with no argument -> use the default
greet()

greet("Rollie")