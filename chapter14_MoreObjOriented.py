#in Python classes are an object that is an instance of class "type". Classes have two tyhpes of variables:
#class variables and instance variables. The variables seen so far are INSTANCE variables.
#INSTANCE variables belong to objects. CLASS variables belong to the object for each class definiton the objects
#they create. You define them in the class.

class Rectangle:
    recs = [] # class variable

    def __init__(self,l,w):
        self.length = l #instance variable
        self.width = w #instance variable
        self.recs.append((self.length,self.width))

rectangle = Rectangle(12,24)
print(Rectangle.recs) #access RECS w/o using global variable

#every class in Python inherits from a parent class called OBJECT
#when you print an object, Python calls a magic method called __repr__. You can override to change what it prints:
class Lion:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
       return self.name

lion = Lion("Ryan")
print(lion)

#operands in an expression must have a magic method the operator can use to evaluate the expression
#for example if you define an __add__ method in a class you can use with the objects it creates
class AlwaysPositive:
    def __init__(self, n):
        self.number = n

    def __add__(self,other):
        return abs(self.number + other.number)

x = AlwaysPositive(10)
y = AlwaysPositive(-20)
print(x+y)

#the IS keyword returns TRUE or FALSE
class Person:
    def __init__(self):
        self.name = "Bobby"

bob = Person()
robert = bob
bobby = Person()
print(bob is robert)
print(bob is bobby)

#use IS keyword to check if a variable is NONE
x = 10
if x is None:
    print("x is none")
else:
    print("x is not none")

x = None
if x is None:
    print("x is none")
else:
    print("x is not none")

#challenge 1
    #add a square_list class variable to a class called SQUARE so that everytime you create
    #a new Square object, the new object gets added to the list
class Square:
    square_list = []

    def __init__(self, n):
        self.name = n
        self.square_list.append(self.name)
square = Square("Alex")
print(Square.square_list)

#challenge 2
    #change the SQUARE class so that when you print a Square object, a message prints telling
    #you the len of each of the four sides of the shape. For example, if you create a square
    #with Square(29) and print it, Python should print 29 by 29 by 29 by 29
class Square:
    def __init__(self, l):
        self.length = str(l)
        print(self.length+" by "+self.length+" by "+self.length+" by "+self.length)

square = Square(29)
print(Square)

#challenge 3
    #write a function that takes two objects as parameters and returns TRUE if they are
    #the same object,and FALSE if not.
def takes_two(x,y):
    if x is y:
        return True
    else:
        return False

takes_two(2,3)
