class pais:
    def __init__(self, n, pop, a):
        self._nome = n
        self.set_populacao(pop)
        self.set_area(a)

    def get_nome(self):
        return self._nome
    
    def get_populacao(self):
        return self._populacao
    
    def get_area(self):
        return self._area

    def set_nome(self, n):
        self._nome = n
    
    def set_populacao(self, pop):
        if pop < 0:
            raise ValueError("População tá inválida pae")
        self._populacao = pop
    
    def set_area(self, a):
        if a <= 0:
            raise ValueError("E essa área inválida pae?")
        self._area = a
    
    def calc_dens(self):
        return self.get_populacao() / self.get_area()


class paisUI:
    @staticmethod
    def menu():
        print("1 - Calcular Densidade")
        print("2 - Sair")
        return int(input())
    
    @staticmethod
    def calculo():
        n = input("Nome da cidade/pais/estado: ")
        pop = float(input("Qual a populacao?: "))
        a = float(input("Qual a area?: "))

        p = pais(n, pop, a)

        print("A densidade é:", p.calc_dens())
    
    @staticmethod
    def main():
        while True:
            op = paisUI.menu()
            if op == 1:
                paisUI.calculo()
            elif op == 2:
                break


paisUI.main()