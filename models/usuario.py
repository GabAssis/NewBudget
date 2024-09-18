import enum

from sqlalchemy import Column, Integer, String, Enum

from utils.database import Base


class Role(enum.Enum):
    ADMIN = 'Admin'
    USUARIO = 'Usuario'

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome_usuario = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)
    email = Column(String, nullable=False)
    nome_completo = Column(String)
    role = Column(Enum(Role))

    def __repr__(self):
        return f"<Usuario(nome_usuario='{self.nome_usuario}', email='{self.email}')>"
