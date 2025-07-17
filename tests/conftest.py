import pytest
from app.infra.db.database import SessionLocal


@pytest.fixture(scope="function")
def db_session():
    """
    Fixture que fornece uma sessão de banco de dados temporária.
    Encerra a sessão após o teste.
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
