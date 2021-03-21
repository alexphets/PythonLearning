#REGULAR EXPRESSIONS are a sequence of characters that define a search pattern
#create a file called zen.txt then enter command python3 -c"import this"
python3 -c"import this"

#the -c flag tells Python you are going to pass it a string containing Python code
#"import this" prints The Zen of Python

#the GREP command accepts two parameters: a regular expression and filepath of the
#file to search for the pattern defined in the expression
grep Beautiful zen.txt

#BEAUTIFUL is the regular expression. zen.txt is the path. if you typed beautiful lower
#case, it will not match anything. you can use -i to ignore case
grep -i beautiful zen.txt

#use command -o to not print the entire line
grep -o beautiful zen.txt

#you can use regular expressions in python with its built-in library RE. It has a method
#called FINDALL. you pass a regular expression then a string. you can ignore case in FINDALL
#method by passing in re.IGNORECASE to the FINDALL METHOD as 3rd paramter
import re
import os
os.path.join("zen.txt")
with open("zen.txt","r") as f:
     l = f.read()
     l = str(l)
     k = re.findall("BEAUTIFUL",l,re.IGNORECASE)
     print(k)

#you can create regular expressions that match complex patterns by adding special
#characters to them that don't match a character but instead define a rule. Example
#use a ^ to create a regular expression if pattern occurs at beginning of line
grep ^if -i zen.txt

#use $ to match patterns that occur at end of line
grep IDEA.$ -i zen.txt

#to find all matches of a pattern in Python use ^ with re.MULTILINE
import re
import os
os.path.join("zen.txt")
with open("zen.txt","r") as f:
     l = f.read()
     l = str(l)
     k = re.findall("^If",l,re.MULTILINE)
     print(k)

#you can define a pattern that match multiple characters by putting them in brackets
#if you put [abc] in regex it will match a,b,or c.
echo Two too. | grep -i t[ow]o

#to define a pattern in Python to match multiple characters:
import re
string = 'Two too.'
m = re.findall('t[ow]o',string,re.IGNORECASE)
print(m)

#you can match digits in a string with double-brackets [[:digit]]
echo 123 hi 34 hello. | grep -o [[:digit:]]

#use \d in Python
import re
line = "123?34 hello?"

m = re.findall("\d",line,re.IGNORECASE)
print(m)

#an * will add repititon to your regex. "the preceding item will be matched zero or more times"
echo two twoo not too. | grep -o two*

#in regex a  .period matches any character. if you follow a period with an * it instructs
#the regex to match any character between the outside characters
echo __hello__there | grep -o __.*__

#an * is GREEDY and will try to match as much as possible. follow with a ? to make it
#NON-GREEDY in Python, grep does NOT have non-greedy matching
import re

t = "_one_ _two_ _three_"

found = re.findall("_.*?_",t)
for match in found:
    print(match)

#you can escape characters in a regex by prefixing with a character with a \
echo I love $ | grep \\$

import re
line = "I love $"

m = re.findall("\$",line,re.IGNORECASE)
print(m)

#challenge 1
    #write a regex that matches the word DUTCH in The Zen of Python
import re
import os
os.path.join("zen.txt")
with open("zen.txt","r") as f:
     l = f.read()
     l = str(l)
     k = re.findall("DUTCH",l,re.IGNORECASE)
     print(k)

#challenge 2
    #come up wiht a regex that matches all the digits in the string
    #Arizona, 479, 501, 870. California 209, 213, 650
import re
string = 'Arizona, 479, 501, 870. California 209, 213, 650'
m = re.findall('[1234567890]',string,re.IGNORECASE)
print(m)

#challenge 3
    #create a regex that matches any word that starts with any character and is
    #followed by two o's. Then use Python's re module to match boo and loo in the
    #sentence THE GHOST THAT SAYS BOO HAUNTS THE LOO
echo you are a foo | grep foo$

import re
sentence = "The ghost that says boo haunts the loo"
k = re.findall(".oo",sentence,re.IGNORECASE)
print(k)
