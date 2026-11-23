from abc import ABC, abstractmethod
import sqlite3

class DAO(ABC):
    # Classe abstrata (nao estatica): cada DAO concreto herda dela
    # e implementa as operacoes do CRUD sobre o SQLite.
    def __init__(self):
        self._conn = None
        self._nome_bd = "agendamento.db"

    def _abrir(self):
        self._conn = sqlite3.connect(self._nome_bd)

    def _fechar(self):
        self._conn.commit()
        self._conn.close()
        self._conn = None

    def _execute(self, sql, params = ()):
        cursor = self._conn.cursor()
        cursor.execute(sql, params)
        return cursor

    @abstractmethod
    def inserir(self, obj):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def listar_id(self, id):
        pass

    @abstractmethod
    def atualizar(self, obj):
        pass

    @abstractmethod
    def excluir(self, id):
        pass
