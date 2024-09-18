demo_tuple = (3, 5, 55, 45, 66, 34, 44)

x = max(demo_tuple)
print(x)

y = min(demo_tuple)
print(y)

i = iter(demo_tuple)          # Get the iterator object from first
j = reversed(demo_tuple)      # Get the iterator object from last

print(next(i))
print(next(i))
print(next(j))
print(next(j))

z = slice(2, 5, 2)
print(demo_tuple[z])

a = sorted(demo_tuple)
print(a)

b = sum(demo_tuple, 10)
print(b)

# input 

c = input("Enter your name: ")
print(
    "Welcome " + c)


