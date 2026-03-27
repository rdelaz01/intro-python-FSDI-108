"""
A while loop repeats a block of code as long as a condition is truw.
Be carefull - if the condition never becomes FALSE, youle have an infinite loop

while condition:
    # Code block runs as long as condition is True
"""

count = 1 

while count <= 5: 
    print("Count is:", count)
    count += 1 # Assignment operator which adds 1 and loop stops at = 5

# using BREAK to stop the loop

number = 0 

while True: # infinite loop but stops with use of "BREAK"
    print(number)
    number+= 1
    if number == 3:
        break # stops when reaches 3 

# using continue to SKIP an iteration / skipping a specific iteration 

count = 0 

while count < 5:
    count += 1
    if count == 3:
        continue # skips  
    print(count)

# els with while
# THe else block runs when the loop condition becomes FALSE (not by break)

count = 1
while count < 3:
    print(count)
    count+= 1
else:
    print("Loop is finished!")

"""
MINI CHALLENGE 
"""

password = ""       # Empty string
while password != "secret123":   #keeps looping while the password is wrong
    password = input("Enter the password:")   
    if password != "secret123":  # if wrong print will say wrong
        print("Wrong try again!")

# Once the condition is met the loop breaks 
print("Access granted")