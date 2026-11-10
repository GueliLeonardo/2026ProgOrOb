from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.horario import Horario
from models.horariodao import HorarioDAO
from models.atendimento import Atendimento
from models.atendimentodao import AtendimentoDAO
from models.profissional import Profissional
from models.profissionaldao import ProfissionalDAO
from datetime import datetime, timedelta

class Service:
    @staticmethod
    def email_validar(email, tipo, id):
        if email.casefold() == "admin":
            atual = ClienteDAO().listar_id(id) if tipo == "cliente" else None
            if atual == None or atual.get_email() != email:
                raise ValueError("E-mail reservado para o administrador")
            return
        for c in ClienteDAO().listar():
            if c.get_email().casefold() == email.casefold() and not (tipo == "cliente" and c.get_id() == id):
                raise ValueError("E-mail já cadastrado")
        for p in ProfissionalDAO().listar():
            if p.get_email().casefold() == email.casefold() and not (tipo == "profissional" and p.get_id() == id):
                raise ValueError("E-mail já cadastrado")

    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        obj = Cliente(0, nome, email, fone, senha)
        Service.email_validar(email, "cliente", 0)
        ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_listar():
        r = ClienteDAO().listar()
        r.sort(key = lambda obj : obj.get_nome().casefold())
        return r
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        obj = Cliente(id, nome, email, fone, senha)
        Service.email_validar(email, "cliente", id)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        for h in HorarioDAO().listar():
            if h.get_id_cliente() == id:
                raise ValueError("Cliente possui horário agendado e não pode ser excluído")
        ClienteDAO().excluir(id)
    @staticmethod
    def cliente_criar_admin():
        for c in Service.cliente_listar():
            if c.get_email() == "admin": return
        ClienteDAO().inserir(Cliente(0, "admin", "admin", "fone", "1234"))
    @staticmethod
    def cliente_autenticar(email, senha):
        for c in Service.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None        


    @staticmethod
    def servico_inserir(descricao, valor):
        obj = Servico(0, descricao, valor)
        ServicoDAO().inserir(obj)
    @staticmethod
    def servico_listar():
        r = ServicoDAO().listar()
        r.sort(key = lambda obj : obj.get_descricao().casefold())
        return r
    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)
    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)
    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)


    @staticmethod
    def horario_validar_duplicidade(data, id_profissional, id):
        if id_profissional in [None, 0]: return
        for h in HorarioDAO().listar():
            if h.get_id() != id and h.get_id_profissional() == id_profissional and h.get_data() == data:
                raise ValueError("Já existe um horário nessa data e hora para o profissional")

    @staticmethod
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(0, data)
        Service.horario_validar_duplicidade(data, id_profissional, 0)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO().inserir(c)
    @staticmethod
    def horario_listar(): # select com order by
        r = HorarioDAO().listar()
        r.sort(key = lambda obj : obj.get_data())
        return r
    @staticmethod
    def horario_listar_id(id): 
        return HorarioDAO().listar_id(id)
    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(id, data)
        Service.horario_validar_duplicidade(data, id_profissional, id)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO().atualizar(c)
    @staticmethod
    def horario_excluir(id):
        h = HorarioDAO().listar_id(id)
        if h != None and h.get_id_cliente() not in [None, 0]:
            raise ValueError("Horário já agendado por um cliente e não pode ser excluído")
        HorarioDAO().excluir(id)
    @staticmethod
    def horario_listar_disponiveis(id_profissional):
        r = []
        agora = datetime.now()
        for h in Service.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False \
            and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort (key = lambda h : h.get_data())
        return r
    @staticmethod
    def horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo, id_profissional):
        data_inicio = datetime.strptime(data + " " + hora_inicio, "%d/%m/%Y %H:%M")
        data_fim = datetime.strptime(data + " " + hora_fim, "%d/%m/%Y %H:%M")
        if intervalo <= 0: raise ValueError("Intervalo deve ser positivo")
        delta = timedelta(minutes = intervalo)
        datas = []
        x = data_inicio
        while x <= data_fim:
            datas.append(x)
            x = x + delta
        for d in datas:
            Horario(0, d)
            Service.horario_validar_duplicidade(d, id_profissional, 0)
        for d in datas:
            Service.horario_inserir(d, False, None, None, id_profissional)
    @staticmethod
    def horario_visualizar_minha_agenda(id_profissional):
        r = []
        for h in Service.horario_listar():
            if h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort (key = lambda h : h.get_data())
        return r
    @staticmethod
    def horario_visualizar_meus_servicos(id_cliente):  # select com where
        r = []
        for h in Service.horario_listar():
            if h.get_id_cliente() == id_cliente:
                r.append(h)
        r.sort (key = lambda h : h.get_data())
        return r
    @staticmethod
    def horario_confirmar_servico(id_profissional):
        r = []
        for h in Service.horario_listar():
            if h.get_confirmado() == False \
            and h.get_id_cliente() != None and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort (key = lambda h : h.get_data())
        return r

    @staticmethod
    def atendimento_inserir(data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        obj = Atendimento(0, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
        AtendimentoDAO().inserir(obj)
    @staticmethod
    def atendimento_listar():
        r = AtendimentoDAO().listar()
        r.sort(key = lambda obj : obj.get_data())
        return r
    @staticmethod
    def atendimento_listar_id(id):
        return AtendimentoDAO().listar_id(id)
    @staticmethod
    def atendimento_atualizar(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        obj = Atendimento(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
        AtendimentoDAO().atualizar(obj)
    @staticmethod
    def atendimento_excluir(id):
        AtendimentoDAO().excluir(id)


    @staticmethod
    def profissional_inserir(nome, email, especialidade, senha):
        obj = Profissional(0, nome, email, especialidade, senha)
        Service.email_validar(email, "profissional", 0)
        ProfissionalDAO().inserir(obj)
    @staticmethod
    def profissional_listar():
        r = ProfissionalDAO().listar()
        r.sort(key = lambda obj : obj.get_nome().casefold())
        return r
    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)
    @staticmethod
    def profissional_atualizar(id, nome, email, especialidade, senha):
        obj = Profissional(id, nome, email, especialidade, senha)
        Service.email_validar(email, "profissional", id)
        ProfissionalDAO().atualizar(obj)
    @staticmethod
    def profissional_excluir(id):
        for h in HorarioDAO().listar():
            if h.get_id_profissional() == id:
                raise ValueError("Profissional possui horário cadastrado e não pode ser excluído")
        ProfissionalDAO().excluir(id)
    @staticmethod
    def profissional_autenticar(email, senha):
        for c in Service.profissional_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None        
