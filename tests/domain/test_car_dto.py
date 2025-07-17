from app.domain.dto.car_dto import CarDTO

def test_car_dto_valido():
    dto = CarDTO(
        marca="Fiat",
        modelo="Pulse",
        ano=2022,
        combustivel="Flex",
        motorizacao="1.0",
        quilometragem=5000,
        portas=4,
        transmissao="Automática",
        cor="Branco",
        preco=95000.0,
        tipo_carroceria="SUV",
        placa="XYZ-1234",
        revisao="2023-07-01"
    )
    assert dto.modelo == "Pulse"
