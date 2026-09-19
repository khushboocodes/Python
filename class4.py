# Arithmetic operators

# + , - , * , / , //, ** , % ,

a = 12
b = 34
print(a + b)
print(a - b)
print(b - a)

# Python follows BODMAS rule

print (12 * 2)
print (12 / 2)

# flow division // for getting the result in integer
print(45 // 8)

# Exponential operator **
print(5 ** 2) # means power of 2

# Modulus operator % for getting the remainder
print (36 % 7)

# Assignment operators
a = 12
a += 12
print(a)

# Concatenation of strings
a = "Hello"
b = " brother"
c = a + b
print(c)

# 1 error in python is that we cannot concatenate string with integer
""" a = "Hello"
b = 5
c = (a + b)
print(c) """

# to overcome we can use type conversion
a = "Hello"
b = 5
c = (a + str(b))
print(c)

# in *
a = "Hello "
print(a * 5)