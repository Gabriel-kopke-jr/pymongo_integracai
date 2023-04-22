from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from cliente import Cliente
from conta import Conta
from database import Base
import pymongo

from utils import generator_document, adjust_document

connection = create_engine("sqlite://", echo=False)

Base.metadata.create_all(connection)

with Session(connection) as session:


    cliente1 = Cliente(
        nome = "Teste 0001",
        cpf = '000000001',
        endereco = 'rua vazia'
            )
    cliente2 = Cliente(
        nome = "Teste 0002",
        cpf = '000000002',
        endereco = 'rua vazia'
            )
    cliente3 = Cliente(
        nome = "Teste 0003",
        cpf = '000000003',
        endereco = 'rua vazia'
            )
    cliente4 = Cliente(
        nome = "Teste 0004",
        cpf = '000000004',
        endereco = 'rua vazia'
            )


    conta1 =  Conta(tipo = '01', agencia = '00001', num = 1, saldo = 150.00, cliente = 1)
    conta2 =  Conta(tipo = '01', agencia = '00002', num = 2, saldo = 250.00, cliente = 2)
    conta3 =  Conta(tipo ='01', agencia ='00003', num=3, saldo=250.00, cliente=2)
    conta4 =  Conta(tipo = '01', agencia ='00004', num=4, saldo=250.00, cliente=2)


    session.add(cliente1)
    session.add(cliente2)
    session.add(cliente3)
    session.add(cliente4)
    session.add(conta2)
    session.add(conta1)
    session.add(conta3)
    session.add(conta4)
    session.commit()

    statement = select(Conta)
    contas = session.scalars(statement).all()

    statement = select(Cliente)
    clientes = session.scalars(statement).all()

    documentos = generator_document(counts = contas,clients = clientes)

    statement = select(Conta).where((Conta.agencia == '00002'))
    rows = session.scalars(statement).all()
   # print(rows)

    statement = select(Conta).where(Conta.cliente == 2)
    rows = session.scalars(statement).all()
    #print(rows)







uri = "mongodb+srv://usuario:usuario@pymongodio.3kdhgc5.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = pymongo.MongoClient(uri)
mydb = client['pymongodio']
mycol = mydb['contas']


documentos_dict = [adjust_document(doc) for doc in documentos]


for element in documentos_dict:
    mycol.insert_one(element)