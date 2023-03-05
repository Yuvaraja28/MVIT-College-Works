from scipy.integrate import dblquad, tplquad

class CircleArea:
    def __init__(self, r: float):
        self.r = r
        self.calculate()
    def calculate(self):
        first_top = self.r
        first_down = second_down = 0
        second_top = lambda x: ((self.r**2) - (x**2)) ** 0.5
        self.area = 4 * dblquad(lambda y, x: 1, first_down, first_top, second_down, second_top)[0]

class SphereVolume:
    def __init__(self, r: float):
        self.r = r
        self.calculate()
    def calculate(self):
        first_top = self.r
        first_down = second_down = third_down = 0
        second_top = lambda x: ((self.r**2) - (x**2)) ** 0.5
        third_top = lambda x, y: ((self.r**2) - (x**2) - (y**2)) ** 0.5
        self.volume = 8 * tplquad(lambda z, y, x: 1, first_down, first_top, second_down, second_top, third_down, third_top)[0]

def credits():
    print("\n> Thank You for using my Program to Find Area of Circle and Volume of Sphere\n> Made by Yuvaraja.M CSE-B Ist Year")

print("┎"+"─"*39+"┒")
print(" "*2+"This is a Simple Program to Calculate")
print(" "*3+"Area of Circle and Volume of Sphere")
print(" "*4+"Made by Yuvaraja.M CSE-B Ist Year")
print("┖"+"─"*39+"┚")
while True:
    try:
        try: user_input = int(input("┎"+"─"*39+"┒"+"\n  Select any one of the Option\n  [1] Area of Circle\n  [2] Volume of Sphere\n  > "))
        except ValueError: print("  Enter a Valid Input not Characters"); print("┖"+"─"*39+"┚"); continue
        if user_input not in [x for x in range(1, 3)]: print(" Not a Valid Option ! "); print("┖"+"─"*39+"┚"); continue
        if user_input == 1:
            try: area = float(input("  Radius of the Circle : "))
            except ValueError: print("  Enter a Valid Input not Characters"); continue
            print(f"  Area of Circle with {area} radius is {CircleArea(area).area:.2f}")
        elif user_input == 2:
            try: volume = float(input("  Radius of the Sphere : "))
            except ValueError: print("  Enter a Valid Input not Characters"); continue
            print(f"  Volume of Sphere with {volume} radius is {SphereVolume(volume).volume:.2f}")
        else: print(" Not a Valid Option ! ")
        print("┖"+"─"*39+"┚")
        if input("> Do you still want to calculate [yes/no] > ").lower() not in ['yes', 'y']: credits(); break
    except KeyboardInterrupt:
        credits(); break