class ParentClass:

    def __init__(self):
        print("Parent class instance")

    def parent_method(self):
        print("Parents Money")


class ChildClass(ParentClass):
    pass


# c = ChildClass()
# c.parent_method()

# p = ParentClass()
# p.parent_method()

#######################################################################################################################

class RateOfInterest:
    interest = 0.06

    def __init__(self, name, loan):
        self.name = name
        self.loan = loan

    def calc_interest(self):
        print("Total interest: ", self.loan * self.interest)


class Student(RateOfInterest):
    interest = 0.02


s = Student("Simran", 500000)
s.calc_interest()


#######################################################################################################################

#  A class can inherit attributes and methods from more than one class: Multiple Inheritance
class MoveCharacter:
    def move_fwd(self):
        print("Move forward 1 step")

    def move_bwd(self):
        print("Move backword q step")


class JumpCharacter:
    def jump_1level(self):
        print("Jump character 1 level")

    def jump_2level(self):
        print("Jump character 2 level")


class Pokemon(MoveCharacter, JumpCharacter):
    def move_bwd(self):
        print("Pokemon Moving")  # Override


p = Pokemon()
p.move_bwd()
p.jump_1level()


# class Mickey(MoveCharacter, JumpCharacter):
#     pass
#
#
# m = Mickey()
# m.move_fwd()
# m.jump_2level()


###################################################################
# Multilevel Inheritance


class Shinchan(JumpCharacter):
    def move_bwd(self):
        print("Shinchan Moving")


sh = Shinchan()
sh.move_bwd()
print(Shinchan.mro())
