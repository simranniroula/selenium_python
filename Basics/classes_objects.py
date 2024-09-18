class Employee:

    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def greet_person(self):
        print("Hello, Welcome to Sim Academy " + self.fname)


emp1 = Employee('Simran', 'Niroula', 'simran@gmail.com')
emp2 = Employee('Asmita', 'Kafle', 'asmita@gmail.com')
emp3 = Employee('Amrit', 'Yadav', 'amrit@gmail.com')
print(emp1.fname)
print(emp2.fname)

emp1.greet_person()
emp2.greet_person()


# objects and methods

class AreaRect:

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def calculate_area(self):
        return self.l * self.b


area1 = AreaRect(10, 2)
area2 = AreaRect(74, 97)

print(area1.calculate_area())
print(area2.calculate_area())

