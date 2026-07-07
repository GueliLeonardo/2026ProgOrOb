import json
from model.cliente import Cliente


class ClienteDAO:

    def __init__(self, arquivo: str = "clientes.json"):
        self.__arquivo = arquivo
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj: Cliente):
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self) -> list:
        return self.__objetos

    def listar_id(self, id: int) -> Cliente:
        for obj in self.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    def atualizar(self, obj: Cliente):
        for i, c in enumerate(self.__objetos):
            if c.get_id() == obj.get_id():
                self.__objetos[i] = obj
                self.__salvar()
                return
        print(f"Cliente com id {obj.get_id()} não encontrado.")

    def excluir(self, id: int):
        obj = self.listar_id(id)
        if obj is not None:
            self.__objetos.remove(obj)
            self.__salvar()
        else:
            print(f"Cliente com id {id} não encontrado.")


    def __abrir(self):
        try:
            with open(self.__arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.__objetos = [Cliente.from_json(d) for d in dados]
        except (FileNotFoundError, json.JSONDecodeError):
            self.__objetos = []

    def __salvar(self):
        with open(self.__arquivo, "w", encoding="utf-8") as f:
            dados = [obj.to_json() for obj in self.__objetos]
            json.dump(dados, f, indent=4, ensure_ascii=False)