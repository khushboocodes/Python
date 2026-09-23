# IF-ELSE Practice Set

# Que 1: Compare Two Numbers - Take two user inputs and determine which number is greater - or if they are equal.

a = float(input("Tell me first num: "))
b = float(input("Tell me second num: "))

if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} is equal to {b}")


# Que 2: Greet by Gender (m/f) - Accept a gender input ('m" or 'f') and print a greeting like "Hello Sir" or "Hello Ma'am".

gender = input("Enter your gender in character(m, f): ")

if gender == 'm':
    print("Hello Sir")
else:
    print("Hello Ma'am")


# Que 3: Gender with Case Handling - Make the gender check case-insensitive ('M', 'F', 'm', 'f' all valid). If input is invalid, print "Wrong input".

gender = input("Enter your gender in character('M', 'F', 'm', 'f'): ")

if gender == 'M' or gender == 'm':
    print("Hello Sir")
elif gender == 'F' or gender == 'f':
    print("Hello Ma'am")
else:
    print("Wrong input (enter only 'M', 'F', 'm', 'f')")


# Question 4: Even or Odd Checker - Accept a number from the user and check whether it's even or odd using modulo (%).

num = int(input("Enter your number: "))

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# Question 5: Voting Elegibility - Input name and age. If age >= 18, print "Eligible to vote". If not, print how many years are left to become eligible.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Hello {name}, you are eligible to vote")
else:
    print(f"Hello {name}, sorry you can vote after {18 - age} years")


 # Que 6: Day Number to Day Name - Take an integer (1-7) and print the corresponding weekday (1 = Monday, 2 = Tuesday, ... 7 = Sunday). Handle invalid input too.

num = int(input("Enter your Day number(1 to 7): "))

if num == 1:
    print("The Day is Monday")
elif num == 2:
    print("The Day is Tuesday")
elif num == 3:
    print("The Day is Wednesday")
elif num == 4:
    print("The Day is Thursday")
elif num == 5:
    print("The Day is Friday")
elif num == 6:
    print("The Day is Saturday")
elif num == 7:
    print("The Day is Sunday")
else:
    print("Invalid input(enter number from 1 to 7)")


# Que 7: Greatest of three numbers - Accept three numbers and find the greatest one among them using nested if-else. Also find if 2 numbers are equal and also find if all are equal.

a = int(input("Enter first num: "))
b = int(input("Enter second num: "))
c = int(input("Enter third num: "))

if a == b and b == c:
    print("All numbers are equal")
elif a == b or b == c or c == a:
    print("Two numbers are equal")
elif a > b and a > c:
    print(f"{a} is the greatest number")
elif b > a and b > c:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")


# Que 8: Leap Year Calender - Input a year and check if it's a leap year using proper rules: divisible by 4, not by 100 unless divisible by 400.

year = int(input("Enter your year: "))

if year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 != 0 and year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# Que 9:  Shop Discount Calculator - Ask for purchase amount. Apply discounts based on thresholds: e.g., above 1000rs. :- 10% off, above 5000rs. :- 20% off. Print final bill.

bill = float(input("Enter your bill amount: "))

if bill >= 1000 and bill <= 4999:
    print(f"You got a discount of 10% and your final bill is: {(bill*90)/100}")
elif bill >= 5000:
    print(f"You got a discount of 20% and your final bill is: {(bill*80)/100}")
else:
    print("Sorry, no discount")


# Que 10: Vowel or Consonant: Accept a single alphabet character and check if it's a vowel (a, e, i , o, u) or consonant.

char = input("Enter a alphabet: ")

if char in "aeiouAEIOU":
    print("It is a vowel")
else:
    print("It is a consonant")