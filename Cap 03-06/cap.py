class viagem:
    def __init__ (self):
        self.__id = 1
        self.__distancia = 1
        self.__tempo = 1

    def set_id(self, id):
        if id <= 0 or type(id) != int: raise(ValueError("O id deve ser um número inteiro positivo"))
        self.__id = id
    def get_id(self): return self.__id

    def set_distancia(self, dist):
        if dist <= 0: raise(ValueError("Distância não pode ser negativa ou nula"))
        self.__distancia = dist
    def get_distancia(self): return self.__distancia

    def set_tempo(self, temp):
        if temp <= 0 or type(temp) != float: raise(ValueError("O tempo deve ser positivo"))
        self.__tempo = temp
    def get_tempo(self): return self.__tempo

    def velocidade_media(self):
        return self.__distancia / self.__tempo


x = viagem()

x.set_id(1)
x.set_distancia(2943.0)
x.set_tempo(39.5) #39 horas e 30 minutos
print(f"Na viagem {x.get_id()}")
print(f"foram percorridos {x.get_distancia()} km")
print(f"em {x.get_tempo()} h")
print(f"A velocidade média foi de {x.velocidade_media():.2f} km/h")
