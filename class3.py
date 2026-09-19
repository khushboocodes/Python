#Class 3- Strings

a = "NATURE"

print(a[5])
print(a[-1],a[5])

a = "NATURE Beautiful"

print(a[6])

a = "Sheryians Coding"
print(a[0:9:1])

#there are default valuses in slicing

print(a[::])


# Task

a = "Hello I am Data Scientist"
#Extract Hello
#Extract Data
#Extract Scientist

print(a[0:5])
print(a[11:15])
print(a[16:25])


#formated strings

age = 25
des = "Data Scientist"

print(f"hello my age is {age} and my designations is {des}")


#escape sequences

#end line with \n
print("hello my name is khushboo\nand my age is 21")

#tab space with \t
print("hello my name is khushboo\tand my age is 21")

#backspace with \b
print("hello my name is khushboo\b and my age is 21")

#raw string and \nwill not work now
print(r"hello my name is khushboo\nand my age is 21")


a = 0
b = ""
print(bool(a))
print(bool(b))

a = "23"
a = int(a)
print(type(a))

age = int(input("tell your age: "))