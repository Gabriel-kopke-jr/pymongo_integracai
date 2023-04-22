from cliente_output import ClienteView
from conta import Conta


def generator_document(counts: list, clients: list)-> list:
    cliente_output_list = []
    for client in clients:
        id = client.id
        counts_client = []
        for count in counts:
            if count.cliente == id:
                counts_client.append(mapper_conta(count))
        cliente_output = ClienteView(client,counts_client)
        cliente_output_list.append(cliente_output)

    return cliente_output_list

def adjust_document(cliente: ClienteView):
    return {
            'id': cliente.id,
            'nome': cliente.nome,
            'cpf': cliente.cpf,
            'endereco':cliente.endereco,
            'contas':cliente.contas}

def mapper_conta(conta:Conta):
    return {'id' : conta.id,
            'tipo': conta.tipo,
            'agencia' : conta.agencia,
            'num' : conta.num,
            'saldo': conta.saldo,
            'cliente' : conta.cliente
    }