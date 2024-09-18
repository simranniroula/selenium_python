s = "Welcome to software testing tutorial with Simran"

# s[i:j] - slice from i to j
'''
print(s[0])
print(s[-1])
print(s[0:7])
print(s[4:8:2])
print(s[3:])
print(s[10:-3])
print(s[::-1])

r = 'name, age, city'
print(r.index(','))
print(r[0:r.index(',')])
'''
# Format String
x = "Python Class"
y = "Simran Academy"

print("Welcome to" + x + "From" + y)

print("Welcome to %s from %s" % (x, y))

print("Welcome to {1} from {0}".format(x, y))     # recommended approach
print("Welcome to {classname} from {academyname}".format(classname=x, academyname=y))








