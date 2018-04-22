# imports the argv command so we can take command line parameters
from sys import argv

# stores the command line parameters in variables. This script expects 1 command line parameter
script, input_file = argv

# defines a function called print_all that takes one input
def print_all(f):
    # reads the input file and prints it to the screen
    print(f.read())

# defines a function called rewind that takes one input
def rewind(f):
    # moves the position of the file back to the beginning
    f.seek(0)

# defines a function called print a line that takes two inputs
def print_a_line(line_count,f):
    #prints the current value of line_count and the current line in a file
    print(line_count, f.readline())

# opens a file name passed from the command line and stores it in current_file
current_file = open(input_file)

# prints a string
print("First let's print the whole file:\n")

# prints all the contents of the file passed in through command line
print_all(current_file)

# prints a string
print("Now let's rewind, kind of like a tape.")

# calls the function rewind with the variable "current_file" as an input to put the file read position of current_file back at the beginning
rewind(current_file)

# prints a string
print("Let's print three lines:")

# stores the number 1 in variable current_line
current_line = 1

# calls the function "print_a_line" with the number stored in "current_line" and the file stored in "current_file". This will print line_number and the current line in the file
# current_line = 1
print_a_line(current_line, current_file)

# increments current_line
current_line = current_line + 1

# calls the function "print_a_line" with the number stored in "current_line" and the file stored in "current_file". This will print line_number and the current line in the file
# current_line = 2
print_a_line(current_line, current_file)

# increments current_line
current_line = current_line + 1

# calls the function "print_a_line" with the number stored in "current_line" and the file stored in "current_file". This will print line_number and the current line in the file
# current_line = 3
print_a_line(current_line, current_file)