from datetime import *
class paciente:
    def __init__(self, n = str, cpf = str, tele = str, nasc = str ):
        self.__nome = n
        self.__cpf = cpf
        self.__telefone = tele
        self.__nascimento = datetime.strptime('nasc', '%d,%m,%Y')
    def set_nome(self, n):
        if self.__nome.type == str:
            self.__nome = n
        else: raise(ValueError)
    def set_cpf (self, cpf):
        if self.__cpf.type == str:
            self.__cpf = cpf
        else: raise(ValueError)
    def set_telefone (self, tele):
        if self.__telefone.type == str:
            self.__telefone = tele
        else: raise(ValueError)
    def set_nascimento(self, nasc):
        if self.__nascimento.type == int:
            self.__nascimento = nasc
        else: raise(ValueError)
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_telefone(self):
        return self.__telefone
    def get_nascimento(self):
        return self.__nascimento