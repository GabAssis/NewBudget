from sqlalchemy import Column, Integer, String

from utils.database import Base


class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String)
    telefone = Column(String)

    def __repr__(self):
        return f"<Cliente(nome={self.nome}, email={self.email})>"
