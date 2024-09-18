"""
score = 85
if score > 90:
    print("I get an Iphone")
elif 80 < score < 90:
    print("I get a bicycle")
elif 70 < score < 80:
    print("I get a Football")
else:
    print("I do not get anything")
"""
# Loops
# While Loop
"""
x = 0
while x <= 2:
    print(x)
    x = x + 1
    print("inside while loop")
print("out of while loop")

city = "Kathmandu"
x = 0
while x < len(city):
    print(city[x])
    x = x + 1
"""
# Break and Continue

a = 0
b = 0
while a <= 2:
    print(a)
    a = a + 1
#   continue
    print("parent while loop")
    while b < 3:
        print(b)
        b = b+1
        continue
        print("inner lopp")
print("out of the while loop")

# else clause

t = 0
while t <= 6:
    print(t)
    t = t + 1
    if t == 5:
        break
else:
    print("out of while loop")

