#a PACKAGE MANAGER is a program that installs and manages other programs
#a WEB FRAMEWORK is a program to help you build a website
#once you DL a pkg with PIP you can import the module in Python
#PIP installs packages into a folder in your python directory called site-packages.
$ pip install [package_name]==[version_num]
$ pip install Flask==1.1.2

#you can now import the FLASK module in a program
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello,World!"

app.run(port='8000')
