from sqlalchemy import Integer, Column, String

from database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column("id",Integer,primary_key = True,autoincrement=True)
    nome = Column("nome",String(50))
    cpf = Column("cpf",String(9))
    endereco = Column("endereco",String(50))

    def __repr__(self):
        return  f"id : {self.id}, nome = {self.nome}, cpf = {self.cpf}, endereco = {self.endereco} \n"


