from sys import argv

script, filename = argv

txt = open(filename)

print(f"Displaying contents of {filename}:")
print(txt.read())