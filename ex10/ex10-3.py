cat = "cat"
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = f"I'm \\ a \\ {cat}."

fat_cat = """
I'll do a list:
\t* {} food
\t* Fishies
\t* {}nip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat.format(cat, cat))

print('A \'single\' quote in a single quote')
print("A \"double\" quote in a double quote")
print("An ASCII bell is this: \a")
print("I maded an error. It should be, \"I maded\b an error.\"")
print("Form\f feed")
print("ASCII\nlinefeed")
print("Carriage\rReturn")
print("A 16-bit hex value character: \uFFFF")
print("A 32-bit hex value character: \U00000001")
print("I have no idea what \v (vertical tab) does")
print("octal value \333")
print("8 bit hex value: \xAA")