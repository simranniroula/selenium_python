def addition(x, y, a):
    return x + y + a


z = addition(23, 45, 56)
# addition(12, 32)
# addition(34, 23)
print(z)


# arguments in python
# Positional Arguments
def sub_demo(a, b):  # a and b are parameters : Those values that are used defining the functions are parameters
    return a - b


c = sub_demo(8,
             9)  # 8  and 9 are arguments : Calling the function and providing actual value within called function are arguments
print(c)


# Optional Arguments

def sub_demo1(d=5, e=8):
    return d + e


print(sub_demo1(8, 6))
print(sub_demo1((8)))
print(sub_demo1())

# Keyword Argument
print(sub_demo1(e=5))

