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


# # Data Structure's in Python

# # list have same Method's as string [0], [0:2] and [0:-1]
# letters = ['a', 'b', 'c']
# matrix = [[0, 1], [2, 3]]
# zeros = list(range(20))
# combined = zeros + letters
# numbers = list(range(20))
# chars = list("Hello World")
# print(letters)
# print(matrix)
# print(zeros[::2])  # this will return every even index
# print(zeros[::-3])  # this will return every even index
# print(combined)
# print(numbers)
# print(chars)


# # list unpacking in Python

# nums = [1, 2, 3, 3, 5, 6, 456, 4, 7, 500]

# first, sec, third, *other = nums
# firsted, *other, lasted = nums

# print(first, sec, third, other)
# print(firsted, lasted)
# print(other)

# letter_s = ['q', 'b', 'f', 'l']

# # enumerate return index and value otherwise without this item will return
# for index, letter in enumerate(letter_s):
#     print(index, letter)

# letter_s.append('a')
# print(letter_s)

# if 'b' in letter_s:
#     print("b is available")


# letter_s.insert(0, '_')  # to insert at specific location's
# print(letter_s)

# # we can add specific index or not
# letter_s.pop(0)
# print(letter_s.sort())

# letter_s.remove("b")
# print(letter_s)

# del letter_s[0:3]
# print(letter_s)

# letter_s.clear()
# print(letter_s)


items = [
    ('1', 10),
    ('2', 9),
    ('3', 12),
]

# def sort_item(item):
#     return item[1]

# # both are same below one is GoodOne

# items.sort(key=sort_item)
# items.sort(key=lambda item: item[1]) # this one
# print(items)


# Another Method


# x = map(lambda item: item[1], items)
# print(x)
# x = list(map(lambda item: item[1], items))
# print(x)

# for item in x:
#     print(item)


# Again Another Method's for Lambda


# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)


# Again Best One List Comprehension's

# we can use this to destruction's of an Object
price = [item[1] for item in items]
print(price)

# we can use this as a Filter
price = [item[1] for item in items if item[1] >= 10]
print(price)
