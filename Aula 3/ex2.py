class triangulo:
    #atributo - dados que guarda: b - base e h - altura
    def __init__(self):
        self.b = 0
        self.h = 0
    #metodo - cálculo que faz
    def calc_area(self):
      return self.b * self.h / 2
    
x = triangulo()
print("informa base ae")
x.b = float(input())
print("e a altura chefe?")
x.h = float(input())
a = x.calc_area()
print(f"A área do triangulo é: {a:.2f}")

y = triangulo()
print("informa base ae")
y.b = float(input())
print("e a altura chefe?")
y.h = float(input())
a = y.calc_area()
print(f"A área do triangulo é: {a:.2f}")

print(f"1º tri: base = {x.b} e altura = {x.h} area = {x.calc_area():.2f}")
print(f"2º tri: base = {y.b} e altura = {y.h} area = {y.calc_area():.2f}")
