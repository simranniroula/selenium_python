"""
x = 10
y = "training"

z = [10, 20, 30, 40, 50]
a = ["St", "sim", "academy"]
b = [10, "sim", 50.1, 40]

print(b[0])
print(a[2])

print(type(b))
print(b[0:3:2])
"""

# list methods

cities = ["Kathmandu", "Pokhara", "Jhapa", "Biratnagar", "Chitwan"]
print(cities)

# list.append(x) : adds value on the last
cities.append("Lumbini")
print(cities)

# list.insert(i, x)  : adds value in the list wherever we want to add with the help of index
cities.insert(1, "Bhaktapur")
print(cities)

# list.remove(x)  : removes value from the list
cities.remove("Lumbini")
print(cities)

# list.pop(x)   : remove item of particular index
cities.pop(4)
print(cities)

# list.index(x)
print(cities.index("Chitwan"))
print(cities)

# count
print(cities.count("Jhapa"))

# sort

cities.sort()
print(cities)
cities.reverse()
print(cities)

# copy
new_cities = cities.copy()
print(new_cities)

# clear
print(new_cities.clear())

