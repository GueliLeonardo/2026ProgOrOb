
class agua():
    def __init__(self):
        self.vol = 0
        self.litros = 0 
    def calc(self):
        self.vol = self.litros / 1000
        self.vol = round(self.vol, 0)
        if self.vol <= 10:
            print("você deve pagar 38,00")
        elif self.vol > 10 and self.vol <= 20:
            print(f"você deve pagar {38 + (self.vol - 10) * 5.00:.2f}")
        elif self.vol >= 21:
            print(f"você deve pagar {38 + (self.vol - 10) * 5.00 + (self.vol - 20) * 6.00:.2f}")
            
x = agua()
print("informe o volume de água (em litros) que você tem ae")
x.litros = float(input())
x.calc()