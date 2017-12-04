# stores a string with placeholders for future formatting into the variable formatter
formatter = "{} {} {} {}"

# prints the variable formatter with the given values inserted into the placeholder
print(formatter.format(1, 2, 3, 4))
# prints the variable formatter with the given values inserted into the placeholder
print(formatter.format("one", "two", "three", "four"))
# prints the variable formatter with the given values inserted into the placeholder
print(formatter.format(True, False, False, True))
# prints the variable formatter with the given values inserted into the placeholder
print(formatter.format(formatter, formatter, formatter, formatter))
# prints the variable formatter with the given values inserted into the placeholder
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))