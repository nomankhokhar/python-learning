# # Variables

# import math
# Student_count = 1000
# rating = 4.99
# is_published = True
# course_name = "Python Programming"

# # print(Student_count)

# # linter check Syntax Error

# comment = """
# I am Python Learning LOLs Best in the Developer. It's my though but it's may be or may not be true
# """


# print("Start from start : ", comment[1])
# print("Start from End : ", comment[-3])
# print("Slice From 2 to 100 :  ", comment[2:])

# # Quote in Code be Like

# # \'
# # \"
# # \n
# # \\


# # Strings Method's
# course = "   Python \'Course\' with me    "

# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())
# print(course.rstrip())
# print(course.lstrip())


# # If find then return Index otherWise -1
# print(course.find("me"))   # return Index
# print(course.replace("P", 'j'))
# print("swift" not in course)  # Return Boolean Value
# print("me" in course)  # Return Boolean Value


# # Number's in Python

# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)


# print(round(2.6))
# print(abs(-2.6))


# print(math.ceil(2.2))
# print(math.floor(2.2))

# # Type Conversion's


# x = input("X : ")

# # int()
# # float()
# # bool()
# # str()

# y = int(x) + 10

# print(y)
# print(type(y))

# # These values consider False Values

# # ""
# # 0
# # None


# # String number boolean
# # number can int float

# print(bool(""))
# print(bool(0))
# print(bool(None))
# print(bool(100))


# print('\n')

# print(10 > 1)
# print(10 >= 1)
# print(10 < 1)
# print(10 <= 1)
# print(10 != 1)
# print(10 == 10)
# print(10 != "10")


# temperature = -35

# if temperature > 20:
#     print("It's warm")
#     print("Temperature is High then 30")
# elif temperature > 30:
#     print(temperature)
# else:
#     print("It's Cold")

# print("Done")


# #Ternary Operator
# age = 22

# messages = "Eligible" if age >= 18 else "Not Eligible"

# print(messages)


# high_income = True
# good_income = False

# if high_income == True and good_income:
#     print("You are Eligible for loan")

# student = False

# if not student:
#     print("Eligible not work in Boolean case")

# if high_income and good_income:
#     print("You are Eligible for loan")
# else:
#     print("You are not Eligible for load")


# # For loop's in Python's

# for i in range(3):
#     print("Attempt", i + 1, (i+1) * ".")


# for i in range(1, 3):
#     print("Attempt", i + 1, (i+1) * ".")


# for i in range(1, 3, 2):
#     print("Attempt", i + 1, (i+1) * ".")
#     if True:
#         print("Successfull")
#         break

# for i in range(10):
#     for j in range(10):
#         print(i*j)
#     print("\n")


# for x in "Python":
#     print(x)


# for x in [1, 2, 3, 4]:
#     print(x)


# number = 100

# while number > 0:
#     print(number)
#     number //= 2


# command = ""
# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == 'quit':
#         break


# Function's in Function's

# def greet(first_name, last_name):
#     print(f"Welcome {first_name} {last_name}")


# greet("Noman", "Ali")


# def get_greeting(name="No_Name"):
#     return f"Welcome {name}"


# message = get_greeting("Noman Ali")
# file = open("content.txt", "w")
# file.write(message)


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(2, 3, 4))

# msg = 'a'


# def save_user(**user):
#     global msg
#     msg = 'b'
#     print(user['id'])
#     print(user['name'])
#     print(user['age'])


# save_user(id=1, name="Noman", age=22)


# ctrl + HOME
# ctrl + END


# FizzBuzz Problem

# def fizz_buzz(input):
#     if (input % 5 == 0) and (input % 3 == 0):
#         return 'FizzBuzz'
#     if input % 3 == 0:
#         return 'Fizz'
#     elif input % 5 == 0:
#         return 'Buzz'
#     return input


# print(fizz_buzz(7))
