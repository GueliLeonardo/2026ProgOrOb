class circulo:
    def __init__(self):
        self.raio = 0.0
        self.pi = 3.141 

    def set_raio(self, r):
        self.raio = r

    def get_raio(self):
        return self.raio

    def calc_area(self):
        return self.pi * (self.raio ** 2)

    def calc_circunferencia(self):
        return 2 * self.pi * self.raio
    

c = circulo()

c.set_raio(float(input("Digite o raio do círculo: ")))

print("Raio:", c.get_raio())
print("Área:", c.calc_area())
print("Circunferência:", c.calc_circunferencia())