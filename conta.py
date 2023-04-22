from sqlalchemy import Column, String, Integer, Float, ForeignKey

from database import Base



class Conta(Base):
    __tablename__ = "conta"

    id = Column("id",Integer, primary_key=True,autoincrement=True)
    tipo = Column("tipo",String(2))
    agencia = Column("agencia",String(5))
    num = Column("num",Integer)
    saldo = Column("saldo",Float(2))
    cliente = Column("id_cliente",Integer,ForeignKey("clientes.id"),nullable = False)

    def __repr__(self):
        return f'id: {self.id}, tipo: {self.tipo}, agencia: {self.agencia},num: {self.num}, saldo: {self.saldo}, cliente: {self.cliente} \n'

