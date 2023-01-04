import math

class DUAL:
    def __init__(self, compression_ratio: float, cut_off_ratio: float, pressure_ratio: float):
        self.compression_ratio = compression_ratio
        self.cut_off_ratio = cut_off_ratio
        self.pressure_ratio = pressure_ratio 
        self.efficiency_value = self.efficiency()
    def efficiency(self):
        calc_nume = (math.pow(self.cut_off_ratio, GAMMA) * self.pressure_ratio) - 1
        calc_deno = math.pow(self.compression_ratio, (GAMMA - 1)) * ((self.pressure_ratio - 1) + (GAMMA*self.pressure_ratio*(self.cut_off_ratio - 1)))
        calc = calc_nume / calc_deno
        return 1 - calc
    def efficiency_percentage(self, round_off: int = 2):
        return round((self.efficiency_value * 100), round_off)

def credits():
    print("\n> Thank You for using my Program to calculate Dual Cycle Efficiency\n> Made by Yuvaraja.M CSE-B Ist Year")

GAMMA = 1.4
print("┎"+"─"*39+"┒")
print(" "*2+"This is a Simple Program to Calculate")
print(" "*9+"Dual Cycle Efficiency")
print(" "*4+"Made by Yuvaraja.M CSE-B Ist Year")
print("┖"+"─"*39+"┚")
while True:
    try:
        try: compression_ratio = float(input("  Compression Ratio Value : "))
        except ValueError: print("Enter a Valid Input"); continue
        try: cut_off_ratio = float(input("  Cut-Off     Ratio Value : "))
        except ValueError: print("Enter a Valid Input not Characters"); continue
        try: pressure_ratio = float(input("  Pressure    Ratio Value : "))
        except ValueError: print("Enter a Valid Input not Characters"); continue
        print(f"> Dual Cycle Efficiency Value : {DUAL(compression_ratio, cut_off_ratio, pressure_ratio).efficiency_percentage()} %")
    except KeyboardInterrupt:
        credits(); break
        