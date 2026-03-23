#if / else are strickly boolean statements, they can only be true or false
# if statement is used to check if a condition is true, and if it is, it will execute the code inside the if block
#elif statement is used to check if another condition is true, and if it is, it will execute the code inside the elif block
#else statement is used to execute code if none of the previous conditions are true

x = 5

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# short Hand if statement
if x > 5: print("x is greater than 5")
print ("even") if x % 2 == 0 else print("odd") # if x is even, print "even", otherwise print "odd"

#nested if statements
if x > 0:
    if x <20:
        print("x is positive and less than 20")

# combining conditions

age = 18 

if age >= 18 and age <=21:
    print("Age is between 18 and 21")

'''
mini challenge:
1. ask user to enter todays temperature and store it in a variable called temperature 
2. use- if-elif-else statment to classify the temperature:
    if temp >= 86, print "its hot outside"
    if tempt >=68, and temp < 86, print the "the weather is nice"
    if temp >= 50, and temp <68, print "its a bit chilly"
    otherwise, print "its cold outside"(else)
3. create a vairable calle jacket :
set temp to true if temp < 59, otherwise false 
4. Bonus: If jacket is true, print "Better wear a jacket!" , otherwise print "No jacket needed today!"
'''
print("=====todays temp=====")
print("Enter today's temperature: ")
temperature = int(input()) # convert the input to an integer

if temperature >= 86:
    print("It's hot outside")
elif temperature >= 68 and temperature < 86:
    print("The weather is nice")
elif temperature >= 50 and temperature < 68:
    print("It's a bit chilly")
else:
    print("It's cold outside")

jacket = temperature < 59 # set jacket to true if temp < 59, otherwise false
if jacket:
    print("Better wear a jacket!")
else:
    print("No jacket needed today!")
