# import argv variable so we can take command line arguments
from sys import argv

# extract the command line arguments from argv and store them in variables
script, filename = argv

# print a formatted string with the filename command line arugment inserted
print(f"We're going to erase {filename}")
# print a string
print("If you don't want that, hit CTRL-C (^C)")
# print a string
print("if you do want that, hit RETURN.")

# get input from the user on whether or not they want to erase the contents of filename
input("?")

# print a string
print("Opening the file...")
# open the file referenced by filename in write mode (which truncates the file) and store the returned file object in target
target = open(filename, 'w')

# print a string
print("Truncating the file. Goodbye!")
# truncate the file object stored in target
target.truncate()

# print a string
print("Now I'm going to ask you for three lines.")

# get user input for line 1 and store in line1
line1 = input("line 1: ")
# get user input for line 2 and store in line2
line2 = input("line 2: ")
# get user input for line 3 and store in line3
line3 = input("line 3: ")

# print a string
print("I'm going to write these to the file.")

# write string stored in line1 to file object in target
target.write(line1)
# write a newline character to file object in target
target.write("\n")
# write string stored in line2 to file object in target
target.write(line2)
# write a newline character to file object in target
target.write("\n")
# write string stored in line3 to file object in target
target.write(line3)
# write a newline character to file object in target
target.write("\n")

# print a string
print("And finally we close it.")
# close the file object in target.
target.close()