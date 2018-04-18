# defines a function that takes two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints a string with the first argument passed into the function inserted into the output
    print(f"You have {cheese_count} cheeses!")
    # prints a string with the second argument passed into the function inserted into the output
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # prints a string
    print("Man that's enough for a party!")
    # prints a string
    print("Get a blanket.\n")

# prints a string
print("We can just give the function numbers directly:")
# calls the cheese_and_crackers function with 20 and 30 as the arguments being passed in
cheese_and_crackers(20,30)

# prints a string
print("OR, we can use variables from our script:")
# stores a value of 10 in the variable amount_of_cheese
amount_of_cheese = 10
# stores a value of 50 in the variable amount_of_crackers
amount_of_crackers = 50

# calls the cheese_and_crackers function, passing in the values stored in the variables amount_of_cheese and amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints a string
print("We can even do math inside too:")
# calls the cheese_and_crackers function with the results of 1 + 20 and 5 + 6 passed in as the arguments.
cheese_and_crackers(10 + 20, 5 + 6)

# prints a string
print("And we can combine the two, variables and math:")

# calls the cheese_and_crackers function with the results of adding 100 to the value stored in amount_of_cheese and 1000 to the value stored in amount_of_crackers as the arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)