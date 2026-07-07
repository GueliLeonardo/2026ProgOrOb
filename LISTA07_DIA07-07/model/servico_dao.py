import json
from model.servico import Servico


class ServicoDAO:

    def __init__(self, arquivo: str = "servicos.json"):
        self.__arquivo = arquivo
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj: Servico):
        """Insere um novo objeto Servico na lista e salva no arquivo."""
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self) -> list:
        """Retorna todos os objetos Servico da lista."""
        return self.__objetos

    def listar_id(self, id: int) -> Servico:
        """Retorna o objeto Servico com o id informado, ou None se não existir."""
        for obj in self.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    def atualizar(self, obj: Servico):
        """Atualiza os dados de um objeto Servico já existente na lista."""
        for i, s in enumerate(self.__objetos):
            if s.get_id() == obj.get_id():
                self.__objetos[i] = obj
                self.__salvar()
                return
        print(f"Serviço com id {obj.get_id()} não encontrado.")

    def excluir(self, id: int):
        """Remove um objeto Servico da lista a partir do id."""
        obj = self.listar_id(id)
        if obj is not None:
            self.__objetos.remove(obj)
            self.__salvar()
        else:
            print(f"Serviço com id {id} não encontrado.")

    def __abrir(self):
        """Recupera a lista de objetos do arquivo Json."""
        try:
            with open(self.__arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.__objetos = [Servico.from_json(d) for d in dados]
        except (FileNotFoundError, json.JSONDecodeError):
            self.__objetos = []

    def __salvar(self):
        """Grava a lista de objetos no arquivo Json."""
        with open(self.__arquivo, "w", encoding="utf-8") as f:
            dados = [obj.to_json() for obj in self.__objetos]
            json.dump(dados, f, indent=4, ensure_ascii=False)