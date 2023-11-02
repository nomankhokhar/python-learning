# Class: blueprint for creating new objects
# Object: instance of a class

# Class : Human
# Object: JOhn, Mary, Jack, Noman Ali

class Point:
    default_color = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return Point(0, 0)

    def __str__(self):
        return f"${self.x} ${self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def draw(self):
        print(f"draw (${self.x} ${self.y})")

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


Point.default_color = 'yellow'

point = Point(1, 2)
print(point.x, point.y)


print(type(point))
print(isinstance(point, Point))

print(point.default_color)
print(Point.default_color)


point = Point.zero()
point.draw()


# Write at Google Python Magic Method's
# __str__ , __init__ , __add__, __eq__ are usefull magic Method's


point_magic_string_method_S = Point(3, 3)
point_magic_string_method_E = Point(3, 3)

print(point_magic_string_method_S == point_magic_string_method_E)
print(point_magic_string_method_S > point_magic_string_method_E)

combined = point_magic_string_method_E + point_magic_string_method_S

print(combined)


# Another Class Tags


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
print(cloud["python"])
cloud.add("python")
cloud["python"] = 4
print(cloud["python"])
print(cloud._TagCloud__tags)


# Another Product Class

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product(50)
product.price = 10
print(product.price)


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


m = Fish()
m.eat()
m.swim()
print(m.age)


print(isinstance(m,Animal))
print(isinstance(m,Mammal))
print(isinstance(m,Fish))
print(isinstance(m,object))


print(m.age, m.weight)







# Multi Level Inheritance

class Animal:
    def eat(self):
        print("eat")
        
        
        
        
class Bird(Animal):
    def fly(self):
        print("fly")
        

class Chicken(Bird):
    pass


# Above Code is Dirty Level Inheritance bcz Bird is Animal and can fly Chicken is animal but not fly this is wrong Level inheritance at all
        
    
    
# Multiple Inheritance

class Person:
    def greet(self):
        print("Person Greet")
        
        
class Employee:
    def greet(self):
        print("Employee Greet")
        
        
# if Manger do not have greet method then go to next Class Employee
class Manager(Employee , Person):
    def greet(self):
        print("Manager Greet")
        

manager = Manager()
manager.greet()         
  
  
  
#Good Example of Inheritance
  
class Flyer:
    def fly(self):
        pass
    
    
    

class Swimmer:
    def swim(self):
        pass
    
class FlyingFish(Flyer , Swimmer):
    pass


# above is a good example of Multiple Inheritance


from abc import ABC, abstractmethod
class InvalidOperationError(Exception):
    pass


# if any class inherit this class those class should have read method's
class Stream(ABC):
    def __init__(self): 
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True
    
    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already Close")
        self.opened = False
    
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")
        
        
        
class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")
        
        
class MemoryStream(Stream):
    def read(self):
        print("Reading data from Memory")


memory = MemoryStream()

memory.read()




# Polymorphism

from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass



class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")
        
        
def draw(controls):
    for control in controls:
        control.draw()
    
    
ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])






# Extended Built-in Types

class Text(str):
    def _init__(self):
        print(self)
        
    def dublicate(self):
        return self + self
    
    
text = Text("Python")
print(text.lower())
print(text.dublicate())


# when we add in the list this class print a append message while append int class

class TrackableList(list):
    def append(self, object):
        print("Append Called")
        super().append(object)
        
        
list = TrackableList()
list.append("1")




from collections import namedtuple

# this will create Point Class with x and y attribute

Point = namedtuple("Point",["x","y"])
p1 = Point(x=1,y=2)
p2 = Point(x=1,y=2)

print(p1 == p2)