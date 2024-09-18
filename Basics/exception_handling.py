try:
    print("Input first number: ")
    x = int(input())
    print("Input second number: ")
    y = int(input())
    if y == 0:
        raise Exception("The denominator should not be 0")
    print(x/y)
except Exception as e:
    print(e)
    print("Wrong Value entered")
else:
    print("Right value entered")
finally:
    print("This is always executed")
