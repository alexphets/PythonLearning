#you should always create file paths using Python's built-in OS module
#if you open a file using the OPEN method you must close it with CLOSE
import os
os.path.join("tstp")
st = open("test.txt","w")
st.write("this is line five")
st.close()
#there is a second preferred syntax so you don't have to remember to close
import os
os.path.join("tstp")
with open("test.txt","w") as f:
    for i in range (1,5):
        i_str = str(i)
        f.write("this is line "+i_str+",")
        i += 1

#if you want to read a file pass "r" as the 2nd parameter
#you can only call read() on a file once >> assign contents to a variable
import os
os.path.join("tstp")
store = []
with open("test.txt","r") as f:
    store.append(f.read())
print(store)

#Python is built-in module to work with CSV. there is a method WRITER to accept a file object and delimiter
#WRITEROW method accepts list s a parameter and will write to CSV
import os
import csv
os.path.join("tstp","test.csv")
store = []
with open("test.csv","w") as f:
        for i in range (1,5):
            i_str = str(i)
            f.write("this is line "+i_str+",")
            i += 1
with open("test.csv","r") as r:
        j = csv.reader(r,delimiter=",")
        store.append(j)

#challenge 1
    #find a file on your computer and print out the contents
import os
with open("test.txt","r") as r:
    print(r.read())

#challenge 2
    #write a program that asks a question and saves the result to a file
import os
def append_results():
    a = input("who is your favorite basketball player?")
    return str(a)
b = append_results()
with open("fav_nba_players.txt","w") as i:
    i.write(b)

#challenge 3
    #take the items in this list of lists [["Top Gun","Risky Business","Minority Report"],
    #["Titanic","The Revenant","Inception"],"Training Day","Man on Fire","Flight"]] and
    #write them to a CSV file. The data from each list should be a row in the file, with each
    #item in the list separated by a comma
import csv
movies = [["Top Gun","Risky Business","Minority Report"],
["Titanic","The Revenant","Inception"],
["Training Day","Man on Fire","Flight"]]
with open("movies.csv","w") as w:
        u = csv.writer(w,delimiter =",")
        u.writerow(movies[0])
        u.writerow(movies[1])
        u.writerow(movies[2])
