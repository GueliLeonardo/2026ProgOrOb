from dao_sql.dao import DAO
from models.cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__()
        self._abrir()
        self._execute("""CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            fone TEXT NOT NULL,
            senha TEXT NOT NULL)""")
        self._fechar()

    def inserir(self, obj):
        self._abrir()
        cursor = self._execute("INSERT INTO cliente (nome, email, fone, senha) VALUES (?, ?, ?, ?)",
            (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_senha()))
        obj.set_id(cursor.lastrowid)
        self._fechar()

    def listar(self):
        self._abrir()
        rows = self._execute("SELECT id, nome, email, fone, senha FROM cliente").fetchall()
        self._fechar()
        return [Cliente(*row) for row in rows]

    def listar_id(self, id):
        self._abrir()
        row = self._execute("SELECT id, nome, email, fone, senha FROM cliente WHERE id = ?", (id,)).fetchone()
        self._fechar()
        return Cliente(*row) if row != None else None

    def atualizar(self, obj):
        self._abrir()
        self._execute("UPDATE cliente SET nome = ?, email = ?, fone = ?, senha = ? WHERE id = ?",
            (obj.get_nome(), obj.get_email(), obj.get_fone(), obj.get_senha(), obj.get_id()))
        self._fechar()

    def excluir(self, id):
        self._abrir()
        self._execute("DELETE FROM cliente WHERE id = ?", (id,))
        self._fechar()
