# Imports the argv variable from the system library, which allows us to get parameters from the command line
from sys import argv

# takes the name of the script and the filename parameter from the command line and stores them into python variables
script, filename = argv

# stores the file object referenced by filenamein variable txt
txt = open(filename)

# prints a formatted string with the name of the file passed in from the command line inserted
print(f"Here's your file {filename}:")
# reads the contents of the file object stored in txt and prints them
print(txt.read())

# prints a string
print("Type the filename again:")
# gets an input from the user of a filename to be read
file_again = input("> ")

# opens the file referenced by file_again and stores it in txt_again
txt_again = open(file_again)

# reads the contents of the file object stored in txt_again and prints them
print(txt_again.read())