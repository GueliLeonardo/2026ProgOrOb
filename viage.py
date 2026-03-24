class viagem:
    def __init__(self):
        self.dist = 0
        self.tempo = 0
    def calc_velo(self):
        return self.dist / self.tempo * 60
    def calc_horas(self):
        return self.tempo 
x = viagem()
print("informa a distância (em km) da viagem ae")
x.dist = float(input())
print("e o tempo da viagem (em minutos) chefe?")
x.tempo = float(input())
veloc = x.calc_velo()
horas = x.calc_horas() / 60
print(f"A velocidade média da viagem é: {veloc:.2f} km/h e o tempo gasto em minutos é: {x.tempo} min e o tempo gasto em horas é: {horas:.2f} h")