#you can multiply a string with a number
#you can insert a string in blank curly brackets using format() method

last = "Phetsadakone"
"Alex {}".format(last)

#method split() will divide a string into multiple by character
#method join() will add new characters between every character in a string
"$".join("hello")
#you can turn list of strings into string using join() passing an empty string
words = ["the","fox","jumped","over","the","road"]
phrase = " ".join(words)
phrase

#method strip() to strip leading/trailing whitespaces
#method replace() replaces every occurrence of a defined string with different one
eq = "all animals are equal"
eq = eq.replace("a","@")
eq

#method index() finds the first occurrence of a character of a string
#to ESCAPE quotes, surround the quote with back slashes  \" [quote] \"
print('she said "this"')

#use \n to carriage return a new line
#SLICING is a way to return a set of items from an interable defining start/end index
#you can leave the start/end index empty if you begin or end with them
slice = "hello"
slice[:2]

#challenge 1
    #print every character in the string "CAMUS"

camus = 'camus'
print(camus[0])
print(camus[1])
print(camus[2])
print(camus[3])
print(camus[4])

#chellenge 2
    #write a pgoram that collects two strings from a user, inserts them into the string
    #"Yesterday I wrote a [response_one]. I sent it to [response_two]!" and prints a new string

def collect():
    response_one = input("what medium did you write?")
    response_two = input("where or who did you send it to?")
    response_one = str(response_one)
    response_two = str(response_two)
    return "Yesterday I wrote a {}. I sent it to {}!".format(response_one,response_two)
collect()

#challenge 3
    #use a method to make the string "aldous huxley was born in 1894."
    #grammatically corect by capitalizing the first letter in the sentence

"aldous huxley was born in 1894.".capitalize()

#challenge 4
    #Take the string "Where now? Who now? When now?" and call a method that returns
    #a list that looks like: ["Where now?","Who now?","When now?"].

"Where now? Who now? When now?".split("?")

#challenge 5
    #Take the list ["the","fox","jumped","over","the","fence","."] and turn it
    #into a grammatically correct string.

fox = ["the","fox","jumped","over","the","fence","."]
new_fox = " ".join(fox[0:6])+fox[6]
new_fox.capitalize()

#challenge 6
    #Replace every instance of "s" in "A screaming comes across the sky." with
    #a dollar sign
"A screaming comes across the sky.".replace("s","$")

#challenge 7
    #Use a method to find the first index of the character "m" in the string "Hemingway"
"Hemingway".index("m")

#challenge 8
    #Create the string "three three three" using concatenation, and then again
    #using multiplication
three = "three "
three_concat = three+three+three
three_multi = three*3
print(three_concat)
print(three_multi)

#challenge 9
    #slice the string "It was a bright cold day in April, and the clocks were
    #striking thirteen." to only include the characters before the comma
before_comma = "It was a bright cold day in April, and the clocks were striking thirteen."
before_comma[0:before_comma.index(",")]
