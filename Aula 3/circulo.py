class circulo:
    def __init__(self):
        self.raio = 0
    def calc_circ(self):
        return 2 * 3.14 * self.raio
    def calc_area(self):
        return 3.14 * self.raio ** 2

x = circulo()
print("informa o raio ae")
x.raio = float(input())
area = x.calc_area()
circ = x.calc_circ()
print(f"A área do circulo e a circunferência são, respectivamente: {area:.2f} e {circ:.2f}")
