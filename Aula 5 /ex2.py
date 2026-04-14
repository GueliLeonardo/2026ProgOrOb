class Viagem:
    def __init__(self):
        self.distancia = 0.0
        self.tempo = 0.0
        self.min = 0.0

    def set_distancia(self, d):
        self.distancia = d

    def set_tempo(self, t):
        self.tempo = t

    def set_min(self, m):
        self.min = m

    def get_distancia(self):
        return self.distancia

    def get_tempo(self):
        return self.tempo

    def get_min(self):
        return self.min

    def velocidade(self):
        tempo_total = self.tempo + (self.min / 60)
        if tempo_total == 0:
            return 0
        return self.distancia / tempo_total
    
v = Viagem()

v.set_distancia(float(input("Por favor insira a distância da viagem, em km:")))
v.set_tempo(float(input("Por favor insira as horas gastas na viagem:")))
v.set_min(float(input("Por favor insira os minutos gastos na viagem:")))


print("Distância:", v.get_distancia(), "km")
print("Tempo:", v.get_tempo(), "h e", v.get_min(), "min")
print("Velocidade média:", v.velocidade(), "km/h")