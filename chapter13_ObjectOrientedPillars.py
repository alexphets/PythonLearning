#the four pillars of obect-oriented programming is ENCAPSULATION, ABSTRACTION,
#POLYMORPHISM, and INHERITANCE

#ENCAPSULATION refers to two concepts: 1) objects group variables (state) and methods
#in a single unit - the object. 2) hiding  a class's internal data to prevent the client
#that uses the object from directly accessing it
#Python does not private variables (all public), therefore precede the variable with an
#underscore and programmers will know not to access it
class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        """
        clients can use this pass
        """

    def _unsafe_method(self):
        """
        clients shouldn't use this pass
        """
#ABSTRACTION is the process of "taking away or removing characteristics from something
#in order to reduce it to a set of essential characteristics"
#POLYMORPHISM is "the ability to present the smae interface for differing underlying form (data types)"

#when a child class inherits a method from a parent classs, you can override it by defininig a new
#method with the same name as the inherited method >> METHOD OVERRIDING
class Shape:
    def __init__(self,w,l):
        self.width = w
        self.length = l

    def print_size(self):
        print("""{} by {}""".format(self.width,self.length))
class Square(Shape):
    def area(self):
        return self.width * self.length

    def print_size(self):
        print("""I am {} by {}""".format(self.width,self.length))

a_square = Square(20,20)
a_square.print_size()

#COMPOSITION models the "has a" relationship by storing an object as a variable in another object
class Dog:
    def __init__(self,d,c,o):
        self.dog = d
        self.color = c
        self.owner = o

class Person:
    def __init__(self,n):
        self.name = n

mick = Person("Mick Jagger")
dane = Dog("Ollie","Red",mick)
print(dane.color)

#challenge 1
    #create RECTANGLE and SQUARE classes with a method called CALCULATE_perimeter that calculates
    #the perimeter of the shapes they represent. Create RECTANGLE and SQUARE objects and call
    #the method on both of them
class Rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return self.length * self.width * 2

class Square:
    def __init__(self,l):
        self.length = l

    def calculate_perimeter(self):
        return self.length * 4

rectangle = Rectangle(2,4)
square = Square(2)
rectangle.calculate_perimeter()
square.calculate_perimeter()

#challenge 2
    #define a method in your SQUARE class called change_size that allows you to pass
    #in a number that increases or decreases (if the number is negative) each side
    #of a Square object by that number
class Square:
    def __init__(self,l):
        self.length = l

    def calculate_perimeter(self):
        return self.length * 4

    def change_size(self,l2):
        self.change = l2
        return self.length + self.change

square = Square(2)
square.change_size(-1)

#challenge 3
    #create a class called Shape. Define a method in it called what_am_i that prints
    #"I am a shape" when called. Change your Square and Rectangle classes from the previous
    #challenges to inherit from Shape, create SQUARE and Rectangle objects, and call the new method on both of them
class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    pass

class Square(Shape):
    pass

square = Square()
square.what_am_i()
rectangle = Rectangle()
rectangle.what_am_i()

#challenge 4
    #create a class called Horse and a class called Rider. Use COMPOSITION to model a horse that has a rider
class Horse:
    def __init__(self,c,h,r):
        self.color = c
        self.height = h
        self.rider = r

class Rider:
    def __init__(self,n):
        self.name = n

rider = Rider("Alex Phetsadakone")
horsie = Horse("red",7,rider)
print(horsie.color)
print(horsie.rider.name)
