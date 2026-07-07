class Servico:

    def __init__(self, id: int, descricao: str, valor: float):
        self.__id = id
        self.__descricao = descricao
        self.__valor = valor

    def __str__(self):
        return f"Serviço [id={self.__id}, descrição={self.__descricao}, valor=R${self.__valor:.2f}]"

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_descricao(self) -> str:
        return self.__descricao

    def set_descricao(self, descricao: str):
        self.__descricao = descricao

    def get_valor(self) -> float:
        return self.__valor

    def set_valor(self, valor: float):
        self.__valor = valor

    def to_json(self) -> dict:
        """Converte o objeto Servico em um dicionário (pronto para serializar em JSON)."""
        return {
            "id": self.__id,
            "descricao": self.__descricao,
            "valor": self.__valor
        }

    @staticmethod
    def from_json(dados: dict) -> "Servico":
        """Cria um objeto Servico a partir de um dicionário lido de um JSON."""
        return Servico(dados["id"], dados["descricao"], dados["valor"])