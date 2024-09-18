from utils.database import engine, Base
from models.usuario import Usuario
from models.Cliente import Cliente



Base.metadata.create_all(engine)