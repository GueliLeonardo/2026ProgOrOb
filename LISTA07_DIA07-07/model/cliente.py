class Cliente:
    def __init__(self, id: int, nome: str, email: str, telefone: str):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone

    def __str__(self):
        return f"Cliente [id={self.__id}, nome={self.__nome}, email={self.__email}, telefone={self.__telefone}]"

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str):
        self.__email = email

    def get_telefone(self) -> str:
        return self.__telefone

    def set_telefone(self, telefone: str):
        self.__telefone = telefone

    def to_json(self) -> dict:
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "telefone": self.__telefone
        }

    @staticmethod
    def from_json(dados: dict) -> "Cliente":
        return Cliente(dados["id"], dados["nome"], dados["email"], dados["telefone"])