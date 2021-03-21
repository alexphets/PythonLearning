#methods are called on objects
#list is a CONTAINER that stores objects in a specific order
#lists are MUTABLE >> add/remove objects from the container
#Strings, Lists, and Tuples are INTERABLE
#An object is iterable when you can access each item using a loop

fruit = ["apple","orange","pear"]
fruit.append("peach")
fruit[1] = "watermelon"
"apple" in fruit
"watermelon" not in fruit

#tuple is a CONTAINER  that stores objects in a specifc order. Tuples are IMMUATABLE
#(i.e, geographic coordinates)

mytuple = ("hello","ni hao","hola")
mytuple[1]

#Dictionaries are a CONTAINER used for linking one object to another. Dictionaries are MUTABLE
#MAPPING is the process of linking objects. keys are IMMUTABLE. Values are MUTABLE
#KEY-VALUE pair is the result
my_dict = {"height":5.5,"height1":5.11,"age":30,"age1":32}
#add key-pair
my_dict["height2"] = 5.7
my_dict["age2"] = 28
#delete key-pair
del my_dict["height1"]
my_dict

#use IN keyword to check if a key is in a dictonary. Cannot use IN for values
#python will raise an exception if the key doesn't exist
#a LIST, TUPLE, or DICTIONARY can be a value inside a dictionary

#challenge 1
    #create a lst of your favorite musicians
fav_musicians = ["Blackpink","Kanye West","Frank Ocean","Chris Brown"]
fav_musicians

#challenge 2
    #creata a list of tuples, with each tuple containing the longitude and latitude
    #of somewhere you've lived or visited
vientiane_laos = ("17.9757° N", "102.6331° E")
vientiane_laos

#challenge 3
    #create a dictionary that contains different attributes about you: height, fav color,
    #fav author, etc.

alex_attributes = {"height":5.6,
                    "fav_color":"orange",
                    "fav_author":"Edgar Allen Poe"
                    }
alex_attributes

#challenge 4
    #write a program that let's the user ask your height, fav color, or fav author
    #and returns the result from the dictionary you created in the previous challenge

alex_attributes = {"height":5.6,
                    "fav_color":"orange",
                    "fav_author":"Edgar Allen Poe"
                    }
def about_me():
        alex = input("To know about me, type HEIGHT, COLOR, or AUTHOR")
        alex = str(alex)
        if alex.upper() == "height".upper():
            return alex_attributes["height"]
        elif alex.upper() == "color".upper():
            return alex_attributes["fav_color"]
        elif alex.upper() == "author".upper():
            return alex_attributes["fav_author"]
        else:
            print("I cannot tell you that")
about_me()

#challenge 5
    #create a dictionary mapping your favorite musicians to a list of your fav songs by them

blackpink_songs = ["Love Sick Girls","Stay with Me", "Pretty Savage"]
kanye_songs = ["Father Stretch My Hands","Robocop","Love Lockdown","Through the Wire"]
frank_songs = ["White Ferrari","Forest Gump","Pyramids"]

artists = {}
artists["blackpink"] = blackpink_songs
artists["kanye"] = kanye_songs
artists["frank"] = frank_songs
artists

#challenge 6
    #List, tuples, and dictionaries are just a few of the containers built into Python.
    #research Python sets (a type of container). When would you use a set?
    """
    sets are used to store multiple items in a single variable. The items are UNINDEXED and UNORDERED.
    there are no duplicate values and you cannot add or delete. Use curly brackets for sets {}
    """

    
