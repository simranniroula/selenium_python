class RateOfInterest:
    interest = 0.06  # class variables are accessible to all the instances . They are not tied to particular object

    #    def __init__(self, name, loan, interest):
    def __init__(self, name,
                 loan):  # Instance variable need to be mentioned in self and need to call to access it. They are not tied to particular object. (interest)
        self.name = name
        self.loan = loan

    #   self.interest = interest

    def calc_interest(self):
        print("Total interest: ", self.loan * self.interest)


person1 = RateOfInterest("Manish", 500000)
person1.interest = 0.08
person1.calc_interest()

person1 = RateOfInterest("Joe", 400000)
person1.calc_interest()



