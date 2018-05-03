# assigns the value 30 to the variable people
people = 30
# assigns the value 40 to the variable cars
cars = 40
# assigns the value 15 to the variable trucks
trucks = 15

# determines if the value assigned to cars is greater than the value assigned to people
if cars > people:
    # prints a string if cars > people
    print("We should take the cars.")
# determines if cars < people
elif cars < people:
    # prints a string if cars < people
    print("We should not take the cars.")
# if cars is not > people or < people, runs the block of code
else:
    # prints a string
    print("We can't decide.")

# determines if trucks is greater than cars and if so, runs the indented block of code
if trucks > cars:
    # prints a string
    print("That's too many trucks.")
# if trucks was not greater than cars, determines if trucks is less than cars, and if so, runs the indented block of code
elif trucks < cars:
    # prints a string
    print("Maybe we could take the trucks.")
# if trucks was not greater than cars or less than cars, runs the indented block of code
else:
    # prints a string
    print("We still can't decide")

# if people is greater than trucks, runs the indented block of code
if people > trucks:
    # prints a string
    print("Alright, let's just take the trucks.")
# if people was not greater than trucks, runs the indented block of code
else:
    # prints a string
    print("Fine, let's stay home then.")