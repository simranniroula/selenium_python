# Used to iterate over sequence like list, string, dictionary, set or tuple

# string
city = "Kathmandu"
for c in city:
    print(c)

# List

capital = ["Kathmandu", "New Delhi", "Canberra"]
for c in capital:
    print(c)

# List within list
cities = [["Nepal", "Kathmandu"], ["India", "New Delhi"], ["Australia", "Canberra"]]
for country, city in cities:
    print("Country is " + country + " and city is " + city)

# dictionaries

my_dict = dict(cities)
print(my_dict)

for country, city in my_dict.items():
    print(country, city)
    for s in country:
        print(s)

# Range is built in functions and generated a sequence of numbers

list_demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in range(1, 10, 3):
    print(x)

