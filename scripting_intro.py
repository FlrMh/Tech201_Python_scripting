# Scripting
import datetime
import os
# Scripting = writing short programmes for automation.
# Shorter pieces of code that allow us to do things we would otherwise have to do manually.
# Unlike programs, scripts are one file and do not need to be compiled.
# APIs = tend to use scripts.


# Scripting languages are meant to be easy to understand.
# Programs are very complicated and detailed.
# Scripts use less or no abstraction and not as flexible as programs. But, they are much easier to read and write.

# Scripting is done to complete a certain task.
# Unlike programs, that are built whether or not they are meant to fulfill a task.

# Scripts are almost always written in high-level languages (the higher level the language, the more it mimics real life languages = easy to read) - Python, Bash, Ruby, Node.js.


# Why Python?

# - Open Source.
# - Many libraries.
# - Easy to understand.
# - Large community.
# - Language interoperability (can interact with other language, OS`s and software)


# Why is scripting important for DevOps?

# - Automation -> Doing everything faster.




# We use modules and libraries for scripting.
# 7 core modules in Python:
# - Sys
# - Os
# - Subprocess
# - Math
# - Random
# - DateTime
# - JSON

# Sys module scripts:
import sys
# Module that allows us to interact with the Python environment.
print(sys.version)
# we run it in terminal as that is the general practice on site.
# outputs the version of python we currently use.

# OS module:
# Used to interact with the host OS.
# files and folders manipulation.
print(os.getcwd()) # get current working directory
# os.chdir("C:\Users\flori\PycharmProjects") # change directory
# os.mkdir() # make a new directory

# Subprocess module
# Can be used to create an interact with subprocesses being managed by our python interpreter. e.g run a dif file
import subprocess
subprocess.run(["python", "hello_world.py"]) # [mention "the language", "the file path"]
# make sure the code is working before you automate it through scripting

# Math module
# Used for more complex mathematical operation.
import math
pi = math.pi
pi_string = str(pi)
print("The value of pi is " + pi_string)

# Random module
# Allows us to randomize values in a number of ways.
import random
random = random.randrange(1, 10)
print(random) # 7, next time 7, next time 5, etc.


# DateTime method
# Allows us to get date and time in a number fo ways.
import datetime
whatisthedate = datetime.datetime.now()
print(whatisthedate) # outputs 2023-02-06 14:20:13.843861

# JSON module
# Human readable, used for transporting data between systems.
import json

x = {
    "name": "Chris",
    "age": 30,
    "city": "London"
}
y = json.dumps(x) # transform the data in a json string

print(y)