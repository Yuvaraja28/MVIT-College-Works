import math

class DIESEL:
    def __init__(self, compression_ratio: int, cut_off_ratio: int):
        self.compression_ratio = compression_ratio
        self.cut_off_ratio = cut_off_ratio
        self.efficiency_value = self.efficiency()
    def efficiency(self):
        calc_nume = math.pow(self.cut_off_ratio, GAMMA) - 1
        calc_deno = (GAMMA * math.pow(self.compression_ratio, (GAMMA - 1))) * (self.cut_off_ratio - 1)
        calc = calc_nume / calc_deno
        return 1 - calc
    def efficiency_percentage(self, round_off: int = 2):
        return round((self.efficiency_value * 100), round_off)
        
def credits():
    print("\n> Thank You for using my Program to calculate Diesel Cycle Efficiency\n> Made by Yuvaraja.M CSE-B Ist Year")

GAMMA = 1.4
print("┎"+"─"*39+"┒")
print(" "*2+"This is a Simple Program to Calculate")
print(" "*9+"Diesel Cycle Efficiency")
print(" "*4+"Made by Yuvaraja.M CSE-B Ist Year")
print("┖"+"─"*39+"┚")
while True:
    try:
        try: compression_ratio = float(input("  Compression Ratio Value : "))
        except ValueError: print("Enter a Valid Input"); continue
        try: cut_off_ratio = float(input("  Cut-Off     Ratio Value : "))
        except ValueError: print("Enter a Valid Input not Characters"); continue
        print(f"> Diesel Cycle Efficiency Value : {DIESEL(compression_ratio, cut_off_ratio).efficiency_percentage()} %")
    except KeyboardInterrupt:
        credits(); break
        