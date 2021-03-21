#FOR-loops interate through an interable (i.e., every character in a string,
#every item in a list, etc.)
#You can use for-loops to change an item in a mutable like list
artists = ["Blackpink","The Weeknd","Kanye West"]
i = 0
for artist in artists:
    cap_artist = artists[i]
    cap_artist_new = cap_artist.upper()
    artists[i] = cap_artist_new
    i+=1
artists
#b/c accessing an item is so common, Python has special syntax for this
artists = ["Blackpink","The Weeknd","Kanye West"]
for i, artist in enumerate(artists):
    cap_artist = artists[i]
    cap_artist_new = cap_artist.upper()
    artists[i] = cap_artist_new
artists

#you can use for-loops to move data between mutables
#the built in RANGE function allows you to iterate thru a sequence of integers
for i in range(1,52):
    print(i)

#a WHILE-LOOP only executes if the expression evaluates to true
#an infinite loop is a loop that never ends. you can use ta BREAK-STATEMENT (keyword)
#to stop the loop from running
x = 10
while x > 0:
    print(x)
    x-=1
print("Happy New Year!")

#use a CONTINUE statement to stop the current iteration of the loop and move on to the
#next iteration
for i in range(1,6):
    if i == 3:
        print("skip")
        continue
    print(i)
#you can achieve the same result with a WHILE and CONTINUE statemets
i = 1
while i < 6:
    if i == 3:
        print("skip")
        i += 1
        continue
    print(i)
    i += 1

#NESTED loops have OUTER and INNER loops to be considered nested.
#you can use two for-loops to iterate and add multiple lists
list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i + j)
list3
#you can nest a for-loop in a while loop and vice versa
while input("yes or no?") != "n":
    for i in range(1,3):
        print(i)

#challenge 1
    #print each item in the following list: ["The Walking Dead", "Entourage",
    #"The Sopranos","The Vampire Diaries"]
shows = ["The Walking Dead", "Entourage", "The Sopranos","The Vampire Diaries"]
for i in shows:
    print(i)

#challenge 2
    #print all the numbers from 25 to 50
i = 25
for i in range (25,51):
    print(i)

#challenge 3
    #print each item in the list from the first challenge and their indexes
shows = ["The Walking Dead", "Entourage", "The Sopranos","The Vampire Diaries"]
j = 0
for i in shows:
    print(i)
    print(j)
    j += 1

#challenge 4
    #write a program wtih an infinite loop (with the option to type q to quit) and
    #a list of numbers. Each time through the loop ask the user to guess a number
    #on the list and tell them whether or not they guessed correctly

num_list = [3,23,45,89,99]
i = 1
while i == 1:
    try:
        a = input("guess a number between 1 and 100 (type \"q\" to quit)")
        a = int(a)
        if a in num_list:
            print("you guessed correct!")
        if a not in num_list:
            print("you guessed wrong!")
        if a == "q":
            break
    except ValueError:
        break

#challenge 5
    #multiply all the numbers in the list [8,19,148,4] with all the numbers in
    #the list [9,1,33,83] and append each result to the third list
list1 = [8,19,148,4]
list2 = [9,1,33,83]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i * j)
list3