import os, sys, re

# unix shell

# starting point

# set environment variable
os.environ["PS1"]= "$"
# print(os.environ["PS1"])

# start taking input

while 1:
    command = input(os.environ["PS1"])
    if command == 'exit':
        break

