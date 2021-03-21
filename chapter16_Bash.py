#ECHO is similar to the PRINT function. enter 'python3' and you can begin to start
#using the program. type HISTORY to view recent commands. enter PWD, which stands for
#print working directory
echo Hello, World!

#ABSOLUTE PATH gives the path starting from the root directory
#RELATIVE PATH is starting from the current working directory. if you path
#does not begin fwd slash then bash knows it's a relative path
 /home/Alex/Documents
 Alex/Documents

#CD is change directory followed by the path. LS prints the folders in current dir
cd / #root
ls #prints folders and files

#create a new directory with MKDIR. navigate to home directory (~ is shortcut in Unix)
#and create new folder
cd ~
cd /tstp/tstp2
mkdir tstp3

#move back on directory using cd ..
#delete a direcoty using RMDIR
cd ..
rmdir tstp3

#commands have a concept called FLAGS to allow the issuer to change command behavior.
#values are TRUE or FALSE. by default flags are set to false. if you add a flag to a
#command, Bash sets the value to TRUE. To set a flag to true put one or two hyphens
#in front of the name of the flag.
ls -author

#your OS stores data in hidden files. hidden files start with a period you can view hidden
#files with flag -a The command TOUCH creates a new file
ls -a
touch .self_taught

#use PIPE to pass output of command as input into another. the result is a text file
ls | less

#ENVIRONMENTAL VARIABLES are variables stored in your operating system that programs
#can use to get data about the environment they are running. create new environmental
#variables with EXPORT VARIABLE_NAME=VARIABLE_VALUE
export x=100
echo $x

#you can print the name of your OS user with WHOIAM. since you do not login at the
#root user, you use SUDO to issue commands as such. NEVER issue as sudo if ur not confident
whoami
sudo echo Hello, World!

#challenge 1
    #print "self-taught" in Bash
echo self-taught

#challenge 2
    #navigate to home directory using absolute and relative path
cd /Users/alexphetsadakone/Documents

#challenge 3
    #create an environmental variable called $python_projects that is an absolute path
    #to the working directory where you keep your python files. save the variable in your
    #.profile file and then use the command cd $python_projects to navigate there
/Users/alexphetsadakone/Documents
