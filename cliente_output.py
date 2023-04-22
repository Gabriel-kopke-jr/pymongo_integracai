from cliente import Cliente


class ClienteView:

    def __init__(self,cliente:Cliente,contas: list):
        self.id = cliente.id
        self.nome = cliente.nome
        self.cpf = cliente.cpf
        self.endereco = cliente.endereco
        self.contas = contas

    def __repr__(self):
        return f'id = {self.id}, nome = {self.nome}, cpf = {self.cpf}, endereco = {self.endereco}, contas = {self.contas}'
