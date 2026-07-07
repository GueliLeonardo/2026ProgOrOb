from model.cliente import Cliente
from model.cliente_dao import ClienteDAO
from model.servico import Servico
from model.servico_dao import ServicoDAO


class Service:

    __cliente_dao = ClienteDAO()
    __servico_dao = ServicoDAO()


    @staticmethod
    def cliente_inserir(id: int, nome: str, email: str, fone: str):
        cliente = Cliente(id, nome, email, fone)
        Service.__cliente_dao.inserir(cliente)

    @staticmethod
    def cliente_listar() -> list:
        return Service.__cliente_dao.listar()

    @staticmethod
    def cliente_listar_id(id: int) -> Cliente:
        return Service.__cliente_dao.listar_id(id)

    @staticmethod
    def cliente_atualizar(id: int, nome: str, email: str, fone: str):
        cliente = Cliente(id, nome, email, fone)
        Service.__cliente_dao.atualizar(cliente)

    @staticmethod
    def cliente_excluir(id: int):
        Service.__cliente_dao.excluir(id)


    @staticmethod
    def servico_inserir(id: int, descricao: str, valor: float):
        servico = Servico(id, descricao, valor)
        Service.__servico_dao.inserir(servico)

    @staticmethod
    def servico_listar() -> list:
        return Service.__servico_dao.listar()

    @staticmethod
    def servico_listar_id(id: int) -> Servico:
        return Service.__servico_dao.listar_id(id)

    @staticmethod
    def servico_atualizar(id: int, descricao: str, valor: float):
        servico = Servico(id, descricao, valor)
        Service.__servico_dao.atualizar(servico)

    @staticmethod
    def servico_excluir(id: int):
        Service.__servico_dao.excluir(id)