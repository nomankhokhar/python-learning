# # Class: blueprint for creating new objects
# # Object: instance of a class

# # Class : Human
# # Object: JOhn, Mary, Jack, Noman Ali

# class Point:
#     default_color = 'red'

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @classmethod
#     def zero(cls):
#         return Point(0, 0)

#     def __str__(self):
#         return f"${self.x} ${self.y}"

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y

#     def draw(self):
#         print(f"draw (${self.x} ${self.y})")

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)


# Point.default_color = 'yellow'

# point = Point(1, 2)
# print(point.x, point.y)


# print(type(point))
# print(isinstance(point, Point))

# print(point.default_color)
# print(Point.default_color)


# point = Point.zero()
# point.draw()


# # Write at Google Python Magic Method's
# # __str__ , __init__ , __add__, __eq__ are usefull magic Method's


# point_magic_string_method_S = Point(3, 3)
# point_magic_string_method_E = Point(3, 3)

# print(point_magic_string_method_S == point_magic_string_method_E)
# print(point_magic_string_method_S > point_magic_string_method_E)

# combined = point_magic_string_method_E + point_magic_string_method_S

# print(combined)


# Another Class
