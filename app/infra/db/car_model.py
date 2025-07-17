from sqlalchemy import Column, Integer, String, Float
from app.infra.db.database import Base


class CarModel(Base):
    __tablename__ = "carros"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String)
    modelo = Column(String)
    ano = Column(Integer)
    combustivel = Column(String)
    motorizacao = Column(String)
    quilometragem = Column(Integer)
    portas = Column(Integer)
    transmissao = Column(String)
    cor = Column(String)
    preco = Column(Float)
    tipo_carroceria = Column(String)
    placa = Column(String)
    revisao = Column(String)
