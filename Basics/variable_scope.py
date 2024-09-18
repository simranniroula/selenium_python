# Local Scope Variable : one variable cannot be accessed by another function if it is defined inside function
# here value of x is defined inside the function so it cannot be accessed by var_scope1
def var_scope():
    x = 20
    print(x)


def var_scope1():
    print(x)


var_scope()

# Global Scope Variable

y = 21


def var_scope2():
    print(y)


def var_scope3():
    print(y)


var_scope2()
var_scope3()


# Global Keyword variable

def var_scope4():
    global z
    z = 22
    print(z)


def var_scope5():
    print(z)


var_scope4()
var_scope5()

# LEGB rule: Local -> Enclosing -> Global  -> Built-in

# enclosing   : variable of parent function will be accessible in child function
t = 100


def var_scope6():
    t = 80
    print(t)

    def child():
        t = 60
        print(t)

        def grand_child():
            print(t)

        grand_child()

    child()


var_scope6()
