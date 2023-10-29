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


# items = [
#     ('1', 10),
#     ('2', 9),
#     ('3', 12),
# ]

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

# #we can use this to destruction's of an Object
# price = [item[1] for item in items]
# print(price)

# # we can use this as a Filter
# price = [item[1] for item in items if item[1] >= 10]
# print(price)


# # Combine the two or more list as you want
# listTwo = [10, 20, 30]
# listThird = [11, 22, 33]
# listOne = [1, 2, 3]
# print(list(zip('abcd', listTwo, listOne, listThird)))


# # Stack's LIFO

# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)

# last = browsing_session.pop()

# print(last)

# print(browsing_session)

# print('Redirect', browsing_session[-1])

# if not browsing_session:
#     print('disable')


# #Queue in Python

# from collections import deque

# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
# print(queue)


# queue.popleft()
# print(queue)


# queue.pop()
# print(queue)

# queue.pop()
# print(queue)

# queue.pop()
# print(queue)

# if not queue:
#     print('Empty')


# #$Tuples in Python
# #they are immutable

# point = (1, 2) * 10
# point = (1, 2) + (3, 4)
# print(point)

# x, y, z, *oth = point
# print(x, y, z, *oth)


# #Swapping the Variable's

# x = 10
# y = 11

# print(x, y)

# y, x = x, y

# print(x, y)


# # Arrays in Python
# from array import array

# numbers = array("f", [1, 2, 3])
# numbers[0] = 1.10

# print(numbers)


# # Set in Python
# # these are collections with no Dublicate


# numbers = [2, 3, 4, 5, 5, 5, 5, 5]
# first = set(numbers)
# second = {1, 5}
# # second.add(5)
# # second.remove(5)
# # combine all the diff num's
# print(first | second)
# # extract the same num's
# print(first & second)
# print(first - second)
# print(first ^ second)

# # we cannot index the set to print the values often we use set to implement these operation's

# if 5 in first:
#     print("Yes")


# # Dictionares in Python


# dic_point = {"x": 1, "y": 2}
# print(dic_point)

# # we can define as well this
# point_s = dict(x=1, y=2)
# point_s[1] = 1000
# print(point_s)


# if "a" in point_s:
#     print('A is Available')

# # if available send the object otherwise None or you define 10
# print(point_s.get('a', 10))

# del point_s["x"]

# print(point_s)

# # this will return key
# for value in point_s:
#     print(value, point_s[value])

# # this will return full key value tuple
# for item in point_s.items():
#     print(item)


# # list comprehension's

# values = []

# # Both are same but best is comprehension's

# for x in range(5):
#     values.append(x * 2)

# print(values)

# # this one is comprehension's

# value_s = {x+1: x*2 for x in range(5)}
# print(value_s)


# # Exercise Find Common Word Cound and  then sort base on Count
# sentence = "This is a common interview question"

# char_frequency = {}

# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1

# # Frequency of Each Value

# print(char_frequency)

# # Both are Good Solution But mine is Best One LOL

# most_fre_used_char = 0

# for key in char_frequency:
#     if (char_frequency[key] > most_fre_used_char):
#         most_fre_used_char = char_frequency[key]

# print(most_fre_used_char)

# # Sorting on Frequency Base
# char_frequency_sorted = sorted(
#     char_frequency.items(), key=lambda kv: kv[1], reverse=True)
# print(char_frequency_sorted[0])
