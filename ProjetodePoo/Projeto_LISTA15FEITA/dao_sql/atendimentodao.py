from datetime import datetime
from dao_sql.dao import DAO
from models.atendimento import Atendimento

class AtendimentoDAO(DAO):
    FORMATO = "%Y-%m-%d %H:%M"

    def __init__(self):
        super().__init__()
        self._abrir()
        self._execute("""CREATE TABLE IF NOT EXISTS atendimento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            queixa_principal TEXT,
            historico_saude TEXT,
            avaliacao TEXT,
            prescricao TEXT,
            id_horario INTEGER)""")
        self._fechar()

    @staticmethod
    def _to_obj(row):
        return Atendimento(row[0], datetime.strptime(row[1], AtendimentoDAO.FORMATO),
                           row[2], row[3], row[4], row[5], row[6])

    def inserir(self, obj):
        self._abrir()
        cursor = self._execute("""INSERT INTO atendimento (data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (obj.get_data().strftime(self.FORMATO), obj.get_queixa_principal(), obj.get_historico_saude(),
             obj.get_avaliacao(), obj.get_prescricao(), obj.get_id_horario()))
        obj.set_id(cursor.lastrowid)
        self._fechar()

    def listar(self):
        self._abrir()
        rows = self._execute("SELECT id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario FROM atendimento").fetchall()
        self._fechar()
        return [AtendimentoDAO._to_obj(row) for row in rows]

    def listar_id(self, id):
        self._abrir()
        row = self._execute("SELECT id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario FROM atendimento WHERE id = ?", (id,)).fetchone()
        self._fechar()
        return AtendimentoDAO._to_obj(row) if row != None else None

    def atualizar(self, obj):
        self._abrir()
        self._execute("""UPDATE atendimento SET data = ?, queixa_principal = ?, historico_saude = ?, avaliacao = ?,
            prescricao = ?, id_horario = ? WHERE id = ?""",
            (obj.get_data().strftime(self.FORMATO), obj.get_queixa_principal(), obj.get_historico_saude(),
             obj.get_avaliacao(), obj.get_prescricao(), obj.get_id_horario(), obj.get_id()))
        self._fechar()

    def excluir(self, id):
        self._abrir()
        self._execute("DELETE FROM atendimento WHERE id = ?", (id,))
        self._fechar()
