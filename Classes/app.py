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


# # Another Class Tags


# class TagCloud:
#     def __init__(self):
#         self.__tags = {}

#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.__tags)

#     def __iter__(self):
#         return iter(self.__tags)


# cloud = TagCloud()
# print(cloud["python"])
# cloud.add("python")
# cloud["python"] = 4
# print(cloud["python"])
# print(cloud._TagCloud__tags)


# # Another Product Class

# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value


# product = Product(50)
# product.price = 10
# print(product.price)


# Intertance 

# Animal class also have method's of Animal Class
# m = object

class Animal:
    def __init__(self):
        self.age = 10

    def eat(self):
        print("eat")


class Mammal(Animal):
    
    def __init__(self):
        self.weight = 10
        # this method will be called at the end of the Mammal Object Called
        super().__init__()
        
        
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.walk()
print(m.age)


# m = Fish()
# m.eat()
# m.swim()
# print(m.age)


print(isinstance(m,Animal))
print(isinstance(m,Mammal))
print(isinstance(m,Fish))
print(isinstance(m,object))


print(m.age, m.weight)
