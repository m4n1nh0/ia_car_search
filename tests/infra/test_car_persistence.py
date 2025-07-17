import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.infra.db.car_model import Base, CarModel
from app.infra.db.car_persistence import CarPersistence


@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


def test_buscar_por_filtros(db_session):
    carro = CarModel(marca="Honda", modelo="Civic", ano=2020,
                     combustivel="Flex", motorizacao="2.0", quilometragem=20000,
                     portas=4, transmissao="Automática", cor="Preto", preco=85000,
                     tipo_carroceria="Sedã", placa="ABC-1234", revisao="2023-01-10")
    db_session.add(carro)
    db_session.commit()

    persistence = CarPersistence(db_session)
    resultado = persistence.buscar_por_filtros(marca="Honda")
    assert len(resultado) == 1
    assert resultado[0].modelo == "Civic"
