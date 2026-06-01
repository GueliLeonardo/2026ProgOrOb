class produto: #A classe é um tipo de variável
    def __init__(self): #Os métodos com "__" (INIT E STR POR EXEMPLO) são "métodos mágicos"
        self.__id = 1
        self.__nome = "resenha"
        self.__preco = 15
        self.__avaliacao = 5
    def __str__(self):
        return f"ID: {self.__id} - Nome: {self.__nome} - Preco: {self.__preco} - Avaliação: {self.__avaliacao}"
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo e inteiro")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError('Nome não pode ser vazio')
        self.__nome = nome
    def set_preco(self, preco):
        if preco < 0: raise ValueError('Preço deve ser positivo')
    def set_avaliacao(self, avaliacao):
        if avaliacao < 1 or avaliacao > 5: raise ValueError("Avaliação deve ser de 1 a 5")
        self.__avaliacao = avaliacao
    def get_id(self): return self.__id
    def get_nome(self):return self.__nome
    def get_preco(self): return self.__preco
    def get_avaliacao(self): return self.__avaliacao

prod = produto() #Nome da classe seguido de () chama o __init__
prod.set_id(5)
prod.set_nome("Cafézinho")
prod.set_preco(10)
prod.set_avaliacao(4)

print(prod.get_id())
print(prod.get_nome())
print(prod.get_preco())
print(prod.get_avaliacao())

print(prod)