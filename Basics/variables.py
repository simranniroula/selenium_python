import keyword


username = "Simran"
print(username)
print(type(username))

x = 600
print(x)
y = x
print(y)

print(id(x))
print(id(y))

# Variables Rules

_test = "Gump"
gump1_test = 678

print(_test)
print(gump1_test)

# Variables are Case-sensitive
rcv8_test = 56734
RCV8_test = 12343

print(rcv8_test)
print(RCV8_test)

# cannot use reserved keyword as variables

returnn = 5643

keywordlist = keyword.kwlist
print(keywordlist)
print(keyword.iskeyword("try"))

# Operator precedence

print(5+8-2)

# string

x = "this is a string"
y = 'this is a \'string\' in single quote'   # backslash can be used if you want to use ''in ''

print(x)
print(y[5])

# multiline string

z = '''
this is a 
       multiline
 string
'''
print(z)

# Membership operator
print("is" in x)

