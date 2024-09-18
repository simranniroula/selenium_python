# len(s) : Returns the number if items in an object.

x = "gump vs GUMP and gumP"
print(len(x))

# str() : Converts specified value into a string

y = 12122000
print(str(y))

# find(sub[, start[, end]]) : Searches the string for a specified value and returns the position
z = str(y)
print(z.find("0"))
print(x.find("GUM"))

# index(sub[, start[, end]]) : Searches the string for a specified value and returns the position of value
print(x.index("gumP"))

# upper : Converts string to uppercase
a = x.upper()
print(a)

# lower : Converts string to lowercase

print(x.lower())

# count : Returns the number of times a specified value is found in the string

print(x.count("gum"))

# is upper : Returns true if all characters in  a string are in uppercase
print(a.isupper())

# islower() :  Returns true if all characters in a string are in lowercase
print(a.islower())

# split(sep=None, maxsplit=-1) : Splits the string at the specified separator, and returns a list
print(x.split())

# rstrip([chars]) :  Removes any trailing characters
# lstrip([chars]) : Removes any leading characters

print(x.lstrip())

# replace(old, new[, count]: Replace a specified phrase with another specified phrase

print(x.replace("gum", "pum", 1))

