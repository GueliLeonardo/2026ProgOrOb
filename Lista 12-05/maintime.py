class Time:
    def __init__(self, i: int, n: str, e: str):
        self.id = i
        self.nome = n
        self.estado = e

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_estado(self):
        return self.estado

    def set_nome(self, nome):
        self.nome = nome

    def set_estado(self, estado):
        self.estado = estado

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Estado: {self.estado}"


class Jogador:
    def __init__(self, i: int, idTime: int, n: str, v: int):
        self.id = i
        self.idTime = idTime
        self.nome = n
        self.camisa = v

    def get_id(self):
        return self.id

    def get_idTime(self):
        return self.idTime

    def get_nome(self):
        return self.nome

    def get_camisa(self):
        return self.camisa

    def set_idTime(self, idTime):
        self.idTime = idTime

    def set_nome(self, nome):
        self.nome = nome

    def set_camisa(self, camisa):
        self.camisa = camisa

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Camisa: {self.camisa} | Time: {self.idTime}"


class UI:
    def __init__(self):
        self.times = []
        self.jogadores = []

    def inserir_time(self):
        i = int(input("ID do time: "))
        n = input("Nome do time: ")
        e = input("Estado: ")

        time = Time(i, n, e)
        self.times.append(time)

        print("Time cadastrado!\n")

    def listar_time(self):
        if len(self.times) == 0:
            print("Nenhum time cadastrado.\n")
        else:
            for t in self.times:
                print(t)
            print()

    def atualizar_time(self):
        i = int(input("Digite o ID do time: "))

        for t in self.times:
            if t.get_id() == i:
                novo_nome = input("Novo nome: ")
                novo_estado = input("Novo estado: ")

                t.set_nome(novo_nome)
                t.set_estado(novo_estado)

                print("Time atualizado!\n")
                return

        print("Time não encontrado.\n")

    def excluir_time(self):
        i = int(input("Digite o ID do time: "))

        for t in self.times:
            if t.get_id() == i:
                self.times.remove(t)

                self.jogadores = [
                    j for j in self.jogadores if j.get_idTime() != i
                ]

                print("Time removido!\n")
                return

        print("Time não encontrado.\n")

    def inserir_jogador(self):
        i = int(input("ID do jogador: "))
        idTime = int(input("ID do time: "))
        n = input("Nome do jogador: ")
        v = int(input("Número da camisa: "))

        existe = False

        for t in self.times:
            if t.get_id() == idTime:
                existe = True

        if not existe:
            print("Time não encontrado.\n")
            return

        jogador = Jogador(i, idTime, n, v)
        self.jogadores.append(jogador)

        print("Jogador cadastrado!\n")

    def listar_jogador(self):
        if len(self.jogadores) == 0:
            print("Nenhum jogador cadastrado.\n")
        else:
            for j in self.jogadores:
                print(j)
            print()

    def atualizar_jogador(self):
        i = int(input("Digite o ID do jogador: "))

        for j in self.jogadores:
            if j.get_id() == i:
                novo_nome = input("Novo nome: ")
                nova_camisa = int(input("Nova camisa: "))

                j.set_nome(novo_nome)
                j.set_camisa(nova_camisa)

                print("Jogador atualizado!\n")
                return

        print("Jogador não encontrado.\n")

    def excluir_jogador(self):
        i = int(input("Digite o ID do jogador: "))

        for j in self.jogadores:
            if j.get_id() == i:
                self.jogadores.remove(j)
                print("Jogador removido!\n")
                return

        print("Jogador não encontrado.\n")

    def listar_jogadores_do_time(self):
        idTime = int(input("Digite o ID do time: "))

        encontrou = False

        for j in self.jogadores:
            if j.get_idTime() == idTime:
                print(j)
                encontrou = True

        if not encontrou:
            print("Nenhum jogador encontrado nesse time.\n")

    def transferir_jogador(self):
        idJogador = int(input("ID do jogador: "))
        novoTime = int(input("Novo ID do time: "))

        existe = False

        for t in self.times:
            if t.get_id() == novoTime:
                existe = True

        if not existe:
            print("Time não encontrado.\n")
            return

        for j in self.jogadores:
            if j.get_id() == idJogador:
                j.set_idTime(novoTime)
                print("Jogador transferido!\n")
                return

        print("Jogador não encontrado.\n")

    def main(self):
        while True:
            print("===== MENU =====")
            print("1 - Inserir time")
            print("2 - Listar times")
            print("3 - Atualizar time")
            print("4 - Excluir time")
            print("5 - Inserir jogador")
            print("6 - Listar jogadores")
            print("7 - Atualizar jogador")
            print("8 - Excluir jogador")
            print("9 - Listar jogadores de um time")
            print("10 - Transferir jogador")
            print("0 - Sair")

            op = int(input("Escolha: "))
            print()

            if op == 1:
                self.inserir_time()

            elif op == 2:
                self.listar_time()

            elif op == 3:
                self.atualizar_time()

            elif op == 4:
                self.excluir_time()

            elif op == 5:
                self.inserir_jogador()

            elif op == 6:
                self.listar_jogador()

            elif op == 7:
                self.atualizar_jogador()

            elif op == 8:
                self.excluir_jogador()

            elif op == 9:
                self.listar_jogadores_do_time()

            elif op == 10:
                self.transferir_jogador()

            elif op == 0:
                print("Saindo...")
                break

            else:
                print("Opção inválida!\n")


ui = UI()
ui.main()