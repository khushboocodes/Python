# if else statement

age = int(input("please enter your age - "))

if age >= 18:
    print("hello you can vote")

else:
    print("sorry you cannot vote")

# if else statement is used to check the condition and if the condition is true then it will execute the code inside the if block otherwise it will execute the code inside the else block
# you cannot write any condition in the else statement

# Ternary operator is used to write the if else statement in a single line

age = int(input("please enter your age - "))
print("vote") if age >= 18 else print("not vote")


# elif statement
# elif statement is used to check multiple conditions and if any one condition is true then it will execute the code inside the if block otherwise it will check the next condition and so on

money = int(input("please give me 10,20 or 30rs or above - "))

if money == 10:
    print("I will have a choco bar")

elif money == 20:
    print("I will have a mango dolly")

elif money == 30:
    print("I will have a cone")

else:
    print("I will have a full course meal")



a = 10
b = 40
c = 30

if a > b and a > c:
    print("a is the largest number")

elif b > a and b > c:
    print("b is the largest number")

else:
    print("c is the largest number")