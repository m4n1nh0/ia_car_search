from app.domain.dto.car_dto import CarDTO
from app.domain.entities.car import Car


def test_car_entity_dto_conversion():
    dto = CarDTO(
        marca="Toyota",
        modelo="Corolla",
        ano=2020,
        combustivel="Gasolina",
        motorizacao="2.0",
        quilometragem=45000,
        portas=4,
        transmissao="Automático",
        cor="Prata",
        preco=95000.0,
        tipo_carroceria="Sedã",
        placa="XYZ9A99",
        revisao="2024-01-10"
    )

    car = Car.from_dto(dto)

    assert car.modelo == "Corolla"
    assert car.portas == 4
    assert car.revisao == "2024-01-10"

    novo_dto = car.to_dto()
    assert dto == novo_dto
