class pais():
    def __init__(self):
        self.nome = ""
        self.populacao = 0
        self.area = 0
    def calc_densidade(self):
        return self.populacao / self.area
    def calc_area(self):
        return self.area ** 2
x = pais()
print("informe o nome do país")
x.nome = input()
print("dá a população do país plz")
x.populacao = int(input())
print("e a área do país (em km)?")
x.area = float(input())
area = x.calc_area()
densidade = x.calc_densidade()
print(f"O país {x.nome} tem uma área de {area:.2f} km² e uma densidade populacional de {densidade:.2f} habitantes por km²")

