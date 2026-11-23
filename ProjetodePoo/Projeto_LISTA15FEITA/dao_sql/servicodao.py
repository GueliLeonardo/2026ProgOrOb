from dao_sql.dao import DAO
from models.servico import Servico

class ServicoDAO(DAO):
    def __init__(self):
        super().__init__()
        self._abrir()
        self._execute("""CREATE TABLE IF NOT EXISTS servico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL)""")
        self._fechar()

    def inserir(self, obj):
        self._abrir()
        cursor = self._execute("INSERT INTO servico (descricao, valor) VALUES (?, ?)",
            (obj.get_descricao(), obj.get_valor()))
        obj.set_id(cursor.lastrowid)
        self._fechar()

    def listar(self):
        self._abrir()
        rows = self._execute("SELECT id, descricao, valor FROM servico").fetchall()
        self._fechar()
        return [Servico(*row) for row in rows]

    def listar_id(self, id):
        self._abrir()
        row = self._execute("SELECT id, descricao, valor FROM servico WHERE id = ?", (id,)).fetchone()
        self._fechar()
        return Servico(*row) if row != None else None

    def atualizar(self, obj):
        self._abrir()
        self._execute("UPDATE servico SET descricao = ?, valor = ? WHERE id = ?",
            (obj.get_descricao(), obj.get_valor(), obj.get_id()))
        self._fechar()

    def excluir(self, id):
        self._abrir()
        self._execute("DELETE FROM servico WHERE id = ?", (id,))
        self._fechar()
