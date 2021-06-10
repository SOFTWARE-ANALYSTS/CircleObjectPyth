import math
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def input_attributes(self):
        self.x = int(input("Faka ikho-odineyithi ka x"))
        self.y = int(input("Faka ikho-odineyithi ka y"))
        self.radius = int(input("Faka irediyasi"))

    def perimeter(self):
        d = 2 * (3.14 * self.radius)
        print("Ipherimitha yesekile", d)

    def area(self):
        a = (3.14) * (self.radius * self.radius)
        print (" ieriya yesekile ngu", a)

    def outsideinsidecircle(self):
        distance = math.sqrt((self.x-0) * (self.x-0) + (self.y-0) * (self.y-0))
        if distance < self.radius:
            print("ipoyinti ingaphakthi kwesekile")
        else:
            print("ipoyinti ingaphandle kwesekile")

if __name__ == '__main__':
    c = Circle(4, 5, 6)
    c.input_attributes()
    c.perimeter()
    c.area()
    c.outsideinsidecircle()

