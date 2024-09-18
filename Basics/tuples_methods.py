# Tuples are indexed, allow duplicate values and cannot be modified (immutable)

demo_tuple = (1, 2, 3, 4, 5)
demo_tuple1 = ("Delhi", "Delhi", "Mumbai", "New York", "Melbourne", "Sydney")
demo_tuple2 = (True, False, False, True)
demo_tuple3 = (True, 1, "Delhi", 23.56)

print(demo_tuple1[1])
print(len(demo_tuple3))
print(type(demo_tuple2))

# Tuple Methods

print(demo_tuple1.count("Delhi"))
print(demo_tuple1.index("New York"))
print(demo_tuple1[3])                  # access value

for x in demo_tuple1:
    print(x)

joined_tuple = demo_tuple1 + demo_tuple2
print(joined_tuple)

print(demo_tuple1[1:4])














