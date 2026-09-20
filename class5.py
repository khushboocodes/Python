# Comparison Operators: 6 types

# == , != not equal to, > , < , <= , >=

print((12 == 12)== True)
print((12 != 12)!= False)

# and operator
# if all the conditions are true then it will return true otherwise if any one condition is false then it will return false
# all the conditions needs to be true for the whole statement to be true

print(12 == 12 and 56 != 45)

print(12 == 12 and 56 > 100 and 45 < 100)

# or operator
# if any one condition is true then it will return true otherwise if all the conditions are false then it will return false
# only one condition needs to be true for the whole statement to be true

print(12 == 56 or 45 == 89 or 34 == 78 or 45 == 45)

# not operator
# it will return the opposite of the condition
# i will return true if the condition is false and it will return false if the condition is true

print(not 12 == 12)
print(not 12 == 12 == False)