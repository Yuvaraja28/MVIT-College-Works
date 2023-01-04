import math

class BRAYTON:
    def __init__(self, compression_ratio: int):
        self.compression_ratio = compression_ratio
        self.efficiency_value = self.efficiency()
    def efficiency(self):
        calc = 1 / (math.pow(self.compression_ratio, ((GAMMA - 1) / GAMMA)))
        return 1 - calc
    def efficiency_percentage(self, round_off: int = 2):
        return round((self.efficiency_value * 100), round_off)

def credits():
    print("\n> Thank You for using my Program to calculate Brayton Cycle Efficiency\n> Made by Yuvaraja.M CSE-B Ist Year")

GAMMA = 1.4
print("┎"+"─"*39+"┒")
print(" "*2+"This is a Simple Program to Calculate")
print(" "*8+"Brayton Cycle Efficiency")
print(" "*4+"Made by Yuvaraja.M CSE-B Ist Year")
print("┖"+"─"*39+"┚")
while True:
    try:
        try: compression_ratio = float(input("  Compression Ratio Value : "))
        except ValueError: print("Enter a Valid Input"); continue
        print(f"> Brayton Cycle Efficiency Value : {BRAYTON(compression_ratio).efficiency_percentage()} %")
    except KeyboardInterrupt:
        credits(); break
        