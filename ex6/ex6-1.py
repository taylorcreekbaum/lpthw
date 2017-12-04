# This statement assigns the value of 10 to the variable types_of_people
types_of_people = 10
# This statement stores a formatted string and inserts the value stored in types_of_people into the string. The string is stored in x.
x = f"There are {types_of_people} types of people."

# This statement stores a string into the variable binary
binary = "binary"
# This statement stores a string into the variable do_not
do_not = "don't"
# This statement stores a formatted string and inserts the values stores in binary and do_not into the string. The string is stored in y.
y = f"Those who know {binary} and those who {do_not}."

# This statement prints the string stored in x
print(x)
# This statement prints the string stored in y
print(y)

# This statement prints a string with the string stored in x inserted into it.
print(f"I said: {x}")
# This statement prints a string with the string stored in y inserted into it.
print(f"I also said: '{y}'")

# This statement stores a boolean value into the variable hilarious
hilarious = False
# This statement stores a string with a placeholder for inserting information into the variable joke_evaluation
joke_evaluation = "Isn't that joke so funny?! {}"

# This statment inserts the value stored in hilarious into the placeholder in joke_evaluation and prints the string
print(joke_evaluation.format(hilarious))

# This statment stores a string in the variable w
w = "This is the left side of..."
# This statement stores a string in the variable e
e = "a string with a right side."

# This statment concatenates the strings stored in w and e and prints the result
print(w + e)