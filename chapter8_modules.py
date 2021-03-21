#to use a module you must IMPORT it
#you should import all your modules to the top of the file
import math
math.pow(2,3)

#RANDOM has a function to generate a random integer
import random
random.randint(1,52)

#use STATISTICS to calculate the mean, median, and mode
import statistics
nums = [23,35,24,28,31]
statistics.mean(nums)
statistics.median(nums)
statistics.mode(nums)

#use KEYWORD to check if string is a Python keyword
import keyword
keyword.iskeyword("for")
keyword.iskeyword("football")

#you can solve the problem of not running all the code from a module by
#indenting your code under this statement:
if __name__ == "__main__":
    print("hello")

#challenge 1
    #call a different from the STATISTICS module
import statistics
nums = [23,35,24,28,31]
statistics.variance(nums)

#challenge 2
    #Create a module named CUBED with a function that takes a number
    #as a parameter andreturn the number cubed. import and call the function
    #from another module
