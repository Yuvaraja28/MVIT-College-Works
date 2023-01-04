import math

class OTTO:
    def __init__(self, compression_ratio: float):
        self.compression_ratio = compression_ratio
        self.efficiency_value = self.efficiency()
    def efficiency(self):
        calc = 1 / (math.pow(self.compression_ratio, (GAMMA - 1)))
        return 1 - calc
    def efficiency_percentage(self, round_off: int = 2):
        return round((self.efficiency_value * 100), round_off)

class DIESEL(OTTO):
    def __init__(self, compression_ratio: float, cut_off_ratio: float):
        self.cut_off_ratio = cut_off_ratio
        super().__init__(compression_ratio)
        self.efficiency_value = self.efficiency()
    def efficiency(self):
        calc_nume = math.pow(self.cut_off_ratio, GAMMA) - 1
        calc_deno = (GAMMA * math.pow(self.compression_ratio, (GAMMA - 1))) * (self.cut_off_ratio - 1)
        calc = calc_nume / calc_deno
        return 1 - calc

class BRAYTON(OTTO):
    def __init__(self, compression_ratio: float):
        super().__init__(compression_ratio)
        self.efficiency_value = self.efficiency()
    def efficiency(self):
        calc = 1 / (math.pow(self.compression_ratio, ((GAMMA - 1) / GAMMA)))
        return 1 - calc

class DUAL(OTTO):
    def __init__(self, compression_ratio: float, cut_off_ratio: float, pressure_ratio: float):
        self.cut_off_ratio = cut_off_ratio
        self.pressure_ratio = pressure_ratio 
        super().__init__(compression_ratio)
        self.efficiency_value = self.efficiency()
    def efficiency(self):
        calc_nume = (math.pow(self.cut_off_ratio, GAMMA) * self.pressure_ratio) - 1
        calc_deno = math.pow(self.compression_ratio, (GAMMA - 1)) * ((self.pressure_ratio - 1) + (GAMMA*self.pressure_ratio*(self.cut_off_ratio - 1)))
        calc = calc_nume / calc_deno
        return 1 - calc

def credits():
    print("\n> Thank You for using my Program to calculate Different Cycles\n> Made by Yuvaraja.M CSE-B Ist Year")

GAMMA = 1.4
print("┎"+"─"*39+"┒")
print(" "*2+"This is a Simple Program to Calculate")
print(" "*5+"Different Thermodynamic Cycle Efficiencies")
print(" "*4+"Made by Yuvaraja.M CSE-B Ist Year")
print("┖"+"─"*39+"┚")
while True:
    try:
        try: user_input = int(input("┎"+"─"*39+"┒"+"\n  Select any one of the Option\n  [1] OTTO Cycle\n  [2] Diesel Cycle\n  [3] Brayton Cycle\n  [4] Dual Cycle\n  > "))
        except ValueError: print("  Enter a Valid Input not Characters"); print("┖"+"─"*39+"┚"); continue
        try: compression_ratio = float(input("  Compression Ratio Value : "))
        except ValueError: print("  Enter a Valid Input not Characters"); continue
        if user_input == 1: print(f"  Otto Cycle Efficiency Value : {OTTO(compression_ratio).efficiency_percentage()} %")
        elif user_input == 2:
            try: cut_off_ratio = float(input("  Cut-Off     Ratio Value : "))
            except ValueError: print("  Enter a Valid Input not Characters"); continue
            print(f"  Diesel Cycle Efficiency Value : {DIESEL(compression_ratio, cut_off_ratio).efficiency_percentage()} %")
        elif user_input == 3: print(f"  Brayton Cycle Efficiency : {BRAYTON(compression_ratio).efficiency_percentage()} %")
        elif user_input == 4:
            try: cut_off_ratio = float(input("  Cut-Off     Ratio Value : "))
            except ValueError: print("  Enter a Valid Input not Characters"); continue
            try: pressure_ratio = float(input("  Pressure    Ratio Value : "))
            except ValueError: print("  Enter a Valid Input not Characters"); continue
            print(f"  DuaL   Cycle Efficiency Value : {DUAL(compression_ratio, cut_off_ratio, pressure_ratio).efficiency_percentage()} %")
        else: print(" Not a Valid Option ! ")
        print("┖"+"─"*39+"┚")
        if input("> Do you still want to calculate [yes/no] > ").lower() not in ['yes', 'y']: credits(); break
    except KeyboardInterrupt:
        credits(); break