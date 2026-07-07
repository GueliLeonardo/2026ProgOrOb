import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from service.service import Service


class UI:

    @staticmethod
    def main():
        opcao = -1
        while opcao != 0:
            opcao = UI.menu()

            if opcao == 1:
                UI.cliente_inserir()
            elif opcao == 2:
                UI.cliente_listar()
            elif opcao == 3:
                UI.cliente_atualizar()
            elif opcao == 4:
                UI.cliente_excluir()
            elif opcao == 5:
                UI.servico_inserir()
            elif opcao == 6:
                UI.servico_listar()
            elif opcao == 7:
                UI.servico_atualizar()
            elif opcao == 8:
                UI.servico_excluir()
            elif opcao == 0:
                print("Encerrando o sistema. Até logo!")
            else:
                print("Opção inválida. Tente novamente.")

    @staticmethod
    def menu() -> int:
        print("\n===== MENU =====")
        print("1 - Inserir cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar cliente")
        print("4 - Excluir cliente")
        print("5 - Inserir serviço")
        print("6 - Listar serviços")
        print("7 - Atualizar serviço")
        print("8 - Excluir serviço")
        print("0 - Sair")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    @staticmethod
    def cliente_inserir():
        print("\n-- Inserir Cliente --")
        id = int(input("Id: "))
        nome = input("Nome: ")
        email = input("Email: ")
        fone = input("Telefone: ")
        Service.cliente_inserir(id, nome, email, fone)
        print("Cliente inserido com sucesso!")

    @staticmethod
    def cliente_listar():
        print("\n-- Lista de Clientes --")
        clientes = Service.cliente_listar()
        if not clientes:
            print("Nenhum cliente cadastrado.")
        for c in clientes:
            print(c)

    @staticmethod
    def cliente_atualizar():
        print("\n-- Atualizar Cliente --")
        id = int(input("Id do cliente a atualizar: "))
        cliente = Service.cliente_listar_id(id)
        if cliente is None:
            print("Cliente não encontrado.")
            return
        nome = input("Novo nome: ")
        email = input("Novo email: ")
        fone = input("Novo telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)
        print("Cliente atualizado com sucesso!")

    @staticmethod
    def cliente_excluir():
        print("\n-- Excluir Cliente --")
        id = int(input("Id do cliente a excluir: "))
        Service.cliente_excluir(id)
        print("Cliente excluído (se existia).")

    @staticmethod
    def servico_inserir():
        print("\n-- Inserir Serviço --")
        id = int(input("Id: "))
        descricao = input("Descrição: ")
        valor = float(input("Valor: "))
        Service.servico_inserir(id, descricao, valor)
        print("Serviço inserido com sucesso!")

    @staticmethod
    def servico_listar():
        print("\n-- Lista de Serviços --")
        servicos = Service.servico_listar()
        if not servicos:
            print("Nenhum serviço cadastrado.")
        for s in servicos:
            print(s)

    @staticmethod
    def servico_atualizar():
        print("\n-- Atualizar Serviço --")
        id = int(input("Id do serviço a atualizar: "))
        servico = Service.servico_listar_id(id)
        if servico is None:
            print("Serviço não encontrado.")
            return
        descricao = input("Nova descrição: ")
        valor = float(input("Novo valor: "))
        Service.servico_atualizar(id, descricao, valor)
        print("Serviço atualizado com sucesso!")

    @staticmethod
    def servico_excluir():
        print("\n-- Excluir Serviço --")
        id = int(input("Id do serviço a excluir: "))
        Service.servico_excluir(id)
        print("Serviço excluído (se existia).")


if __name__ == "__main__":
    UI.main()