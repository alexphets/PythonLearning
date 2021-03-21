#built-in function INPUT
kobe = input("what were Kobe's numbers that were retired?")
int_kobe = int(kobe)
if int_kobe == 8:
    print("that's one of them!")
elif int_kobe == 24:
    print("that's one of them!")
else:
    print("that's not one of them.")

#exception handling
try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
    print(a/b)
except (ZeroDivisionError,ValueError):
    if b == 0:
        print("b cannot be zero.")
    else:
        print("invalid input.")

#challenge 1
    #write a function that takes a number as an input and returns that number squared
def squared():
    a = input("what number do you want to square?")
    a = int(a)
    b = a**a
    return b
squared()

#challenge 2
    #create a function that accepts a string as a parameter and prints it
def take_string(x):
    """
    x should be a string
    """
    print(x)
take_string("hello")

#challenge 3
    #write a function that takes three REQ parameters and two optional
def multiple(x,y,z,a=10,b=2):
    """
    all variables should be numbers
    """
    total = ((x+y+z)*a)/b
    return total
multiple(2,2,2)

#challenge 4
    #write a program with two functions. First function should take an integer as a parameter
    #and return the result divided by 2. Second function should ake an integer as a parameter
    #and return the result multiplied by 4. Call the first function, save the result as a variable
    #and pass it as a parameter to the second function
def first(x):
    return x/2

def second(y):
    return y*4

a = first(4)
second(a)

#challenge 5
    #write a function that converts a string to a float and returns the result. Use exception
    #handling to catch the exception that could occur

def convert():
    """
    function takes string and converts to float.
    Uses exception handling.
    """
    try:
        x = input("what number do you want as a float?")
        x = float(x)
        print(x)
    except (ValueError):
        print("that is not a number")

convert()

#challenge 6
    #Add a docstruing to all of the functions you wrote in challenges 1-5
