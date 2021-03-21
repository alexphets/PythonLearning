#procedural programming paradigm is sequence of steps movimng toward a solution "do this, then that"
#you store data in global variables and manipulate it with functions
a = 0
def increment():
    global a
    a += 1
#functional programming relies on function that do not change global state. they only use
#parameters that are passed and values returned in the function
def increment(a):
    a + 1

#object oriented programming classes define objects that can interact with eachother.
#INSTANCE and OBJECT can be used interchangeably
class Orange:
    def __init__(self,w,c):
        self.weight = w
        self.color = c
        print("Created!")
or1 = Orange(10,"dark orange")
print(or1)
#you change the value of an instance variable with the object and variable name
class Orange:
    def __init__(self,w,c):
        self.weight = w
        self.color = c
        print("Created!")
or1 = Orange(10,"dark orange")
or1.weight = 100
or1.color = "orange"
print(or1.weight)
print(or1.color)
#you can define multiple methods in a class
class Orange:
    def __init__(self,w,c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self,days,temp):
        self.mold = days * temp

or1 = Orange(8,"blue")
print(or1.mold)
or1.rot(10, 78)
print(or1.mold)

#challenge 1
    #define a class called Apple with four instance variables that represent four attributes of an apple
class Apple:
    def __init__(self,c,w,d,t):
        self.color = c
        self.weight = w
        self.diamater = d
        self.type = t
apple = Apple("green",10,3,"green apple")
print(apple.color)

#challenge 2
    #create CIRCLE class with a method called AREA that calculates and returns its area
    #then create a CIRCLE object, call area on it, and print the result. Use Python's PI
    #function in the built-in MATH module
import math
class Circle:
    def __init__(self,r):
        self.radius = r

    def area(self):
        return (self.radius**2)*math.pi

circle = Circle(2)
print(circle.area())

#challenge 3
    #Create a Triangle class with a method called AREA that calculates and returns its area.
    #Then create a Triangle object, call AREA on it, and print the result
class Triangle:
    def __init__(self,l,h):
        self.length = l
        self.height = h

    def area(self):
        return (self.length * self.height)/2

triangle = Triangle(6,2)
print(triangle.area())

#challenge 4
    #make a hexagon class with a method called calculate_perimeter that calculates and
    #returns its perimeter. Then create a Hexagon object, call calculate_perimeter
    #on it and print the result
class Hexagon:
    def __init__(self,a):
        self.length = a

    def calculate_perimeter(self):
        return self.length * 6

hexagon = Hexagon(6)
print(hexagon.calculate_perimeter())
