from dao_sql.dao import DAO
from models.profissional import Profissional

class ProfissionalDAO(DAO):
    def __init__(self):
        super().__init__()
        self._abrir()
        self._execute("""CREATE TABLE IF NOT EXISTS profissional (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            especialidade TEXT NOT NULL,
            senha TEXT NOT NULL)""")
        self._fechar()

    def inserir(self, obj):
        self._abrir()
        cursor = self._execute("INSERT INTO profissional (nome, email, especialidade, senha) VALUES (?, ?, ?, ?)",
            (obj.get_nome(), obj.get_email(), obj.get_especialidade(), obj.get_senha()))
        obj.set_id(cursor.lastrowid)
        self._fechar()

    def listar(self):
        self._abrir()
        rows = self._execute("SELECT id, nome, email, especialidade, senha FROM profissional").fetchall()
        self._fechar()
        return [Profissional(*row) for row in rows]

    def listar_id(self, id):
        self._abrir()
        row = self._execute("SELECT id, nome, email, especialidade, senha FROM profissional WHERE id = ?", (id,)).fetchone()
        self._fechar()
        return Profissional(*row) if row != None else None

    def atualizar(self, obj):
        self._abrir()
        self._execute("UPDATE profissional SET nome = ?, email = ?, especialidade = ?, senha = ? WHERE id = ?",
            (obj.get_nome(), obj.get_email(), obj.get_especialidade(), obj.get_senha(), obj.get_id()))
        self._fechar()

    def excluir(self, id):
        self._abrir()
        self._execute("DELETE FROM profissional WHERE id = ?", (id,))
        self._fechar()
