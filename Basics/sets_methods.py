demo_set1 = {10, 20, 30, 40, 50, 50}                   # can not set duplicate value
demo_set2 = {10, "sim", 30.5, 55, "academy"}
demo_set3 = {"50", "100"}

print(demo_set1)
print(len(demo_set3))
print("sim" in demo_set2)   # membership operator


demo_set4 = {"jhapa", "pokhara", "ktm", "bhaktapur"}
demo_set5 = {"jhapa", "pokhara", "ktm", "bhaktapur", "sydney", "new york", "delhi"}

# demo_set4.add("Gold Coast")
# print(demo_set4)
# demo_set4.remove("bhaktapur")
# print(demo_set4)
# demo_set4.discard("ktm")
# print(demo_set4)

# Union and Intersection
demo_set6 = demo_set1.union(demo_set5)
print(demo_set6)

demo_set7 = demo_set1.intersection(demo_set2)
print(demo_set7)

demo_set6 = demo_set1.symmetric_difference(demo_set2)
print(demo_set6)

demo_set7 = demo_set1.symmetric_difference_update(demo_set2)
print(demo_set7)

demo_set8 = demo_set4.issubset(demo_set5)
print(demo_set8)

demo_set9 = demo_set5.issuperset(demo_set4)
print(demo_set9)

