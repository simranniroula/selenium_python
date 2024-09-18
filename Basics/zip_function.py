list1 = ["India", "USA", "Nepal", "UK"]
list2 = ["Pune", "New York", "Kathmandu", "London", "Sydney"]

# s = zip(list1,list2)
# print(list(s))

# List and Tuple both can be used in Zip

for x,y in zip(list1, list2):
    print(x, y)

total_cost = [25, 45, 55, 65]
sale_price = [55, 65, 45, 60]

for a,b in zip(total_cost,sale_price):
    print(b-a)

