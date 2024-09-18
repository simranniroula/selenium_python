# They are changeable and do not allow duplicate value
"""
demo_dict = {}
print(type(demo_dict))

demo_dict1 = {"name": "Sana", "age": 18, "address": "Kathmandu"}
demo_dict2 = {1: 20, 2: 40, 3: 60, 4: 80}
demo_dict3 = {"address": 20, 4: "Kathmandu"}

print(demo_dict1["name"])

# add key value pair
demo_dict3['prod'] = 'produrl'
print(demo_dict3)

demo_dict2[5]= 100
print(demo_dict2)
# remove
demo_dict2.pop(5)
print(demo_dict2)
"""

env = {"qa": "testurl", "uat": "uaturl", "preprod": "preprodurl"}

# get()   Returns the value for specified key in the dictionary
print(env.get("preprod"))

# keys()   Returns a copy of dictionary's key
print(env.keys())

# items()  Returns a copy for dictionary's key value pair
print(env.items())

# Values  Returns a copy of values in the dictionary
print(env.values())

# pop()  Removes the item with specified key
print(env.pop("uat"))

# popitem()  Remove the arbitrary key: value pair
print(env.popitem())

# update()    Adds the specified key-value pairs to dictionary
env.update({"prod": "produrl"})
print(env)

# copy() Returns a copy of dictionary
env_copy = env.copy()
print(env_copy)

# clear()  Removes all the elements from the dictionary
env_copy.clear()
print(env_copy)
