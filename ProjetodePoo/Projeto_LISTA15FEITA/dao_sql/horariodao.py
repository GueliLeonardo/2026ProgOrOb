from datetime import datetime
from dao_sql.dao import DAO
from models.horario import Horario

class HorarioDAO(DAO):
    FORMATO = "%Y-%m-%d %H:%M"

    def __init__(self):
        super().__init__()
        self._abrir()
        self._execute("""CREATE TABLE IF NOT EXISTS horario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            confirmado INTEGER NOT NULL,
            id_cliente INTEGER,
            id_servico INTEGER,
            id_profissional INTEGER)""")
        self._fechar()

    @staticmethod
    def _to_obj(row):
        obj = Horario(row[0], datetime.strptime(row[1], HorarioDAO.FORMATO))
        obj.set_confirmado(bool(row[2]))
        obj.set_id_cliente(row[3])
        obj.set_id_servico(row[4])
        obj.set_id_profissional(row[5])
        return obj

    def inserir(self, obj):
        self._abrir()
        cursor = self._execute("""INSERT INTO horario (data, confirmado, id_cliente, id_servico, id_profissional)
            VALUES (?, ?, ?, ?, ?)""",
            (obj.get_data().strftime(self.FORMATO), int(obj.get_confirmado()),
             obj.get_id_cliente(), obj.get_id_servico(), obj.get_id_profissional()))
        obj.set_id(cursor.lastrowid)
        self._fechar()

    def listar(self):
        self._abrir()
        rows = self._execute("SELECT id, data, confirmado, id_cliente, id_servico, id_profissional FROM horario").fetchall()
        self._fechar()
        return [HorarioDAO._to_obj(row) for row in rows]

    def listar_id(self, id):
        self._abrir()
        row = self._execute("SELECT id, data, confirmado, id_cliente, id_servico, id_profissional FROM horario WHERE id = ?", (id,)).fetchone()
        self._fechar()
        return HorarioDAO._to_obj(row) if row != None else None

    def atualizar(self, obj):
        self._abrir()
        self._execute("""UPDATE horario SET data = ?, confirmado = ?, id_cliente = ?, id_servico = ?, id_profissional = ?
            WHERE id = ?""",
            (obj.get_data().strftime(self.FORMATO), int(obj.get_confirmado()),
             obj.get_id_cliente(), obj.get_id_servico(), obj.get_id_profissional(), obj.get_id()))
        self._fechar()

    def excluir(self, id):
        self._abrir()
        self._execute("DELETE FROM horario WHERE id = ?", (id,))
        self._fechar()
