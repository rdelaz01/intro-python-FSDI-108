#1. Arithmatic Operators 

x = 1
y = 2
res = 0

res = x + y
print(res)


res = x - y
print(res)


res = x * y
print(res)

res = x / y
print(res)

#2. Assignment Operators
# = mean to put a value into a variable
x = 5
x += 5 # x = x + 5
x -= 5 # x = x - 5
x *= 5 # x = x * 5
x /= 5 # x = x / 5
print(x)


#3. Comparison Operators
# Used to compare two values and return a boolean (True or False)
# same as if else statements in other programming languages

# == () equal to
# != (not equal to)
# > (greater than)
# < (less than)
# >= (greater than or equal to)
# <= (less than or equal to)
# "and" both must be true
# "or" either one can be true
# "not" negates the value (True becomes False, and False becomes True)

x = 3
y = 10
z = 10

print(x == y and y == z) # False because x is not equal to y
print(x == z or y == z) # True because y is equal to z
print(not(x == y)) # True because x is not equal to y

# 5. Logical Operators - used to compare the objects, not if theyre equal
# but if theyre actually the same object
# is check if to=wo things are the same object in memory
# is not check if two things are not the same object in memory


x =3 
y = 3 
print(x is y) # True because x and y are the same object in memory
print(x is not y) # False because x and y are the same object in memory


# 6. Membership Operators - used to check if a value is in a sequence (like a list, tuple, or string)
# in check if a value is in a sequence
# not in check if a value is not in a sequence

x = [1, 2, 3, 4, 5] # this is a list

print(4 in x) # True because 4 is in the list x
print(6 in x) # False because 6 is not in the list x
print(6 not in x) # True because 6 is not in the list x

