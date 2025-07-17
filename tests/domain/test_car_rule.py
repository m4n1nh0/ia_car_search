from app.domain.rules.car_rule import CarRule
from app.domain.dto.car_dto import CarDTO


class FakeCarPersistence:
    def buscar_por_filtros(self, limit=5, **filtros):
        return [{
            "marca": "Fiat",
            "modelo": "Uno",
            "ano": 2020,
            "combustivel": "Flex",
            "motorizacao": "1.0",
            "quilometragem": 40000,
            "portas": 4,
            "transmissao": "Manual",
            "cor": "Preto",
            "preco": 35000.0,
            "tipo_carroceria": "Hatch",
            "placa": "ABC-1234",
            "revisao": "2023-10-10"
        }]


def test_buscar_veiculos_filtrados_com_mock():
    car_rule = CarRule(FakeCarPersistence())
    resultado = car_rule.buscar_veiculos_filtrados({"marca": "Fiat"})
    assert len(resultado) == 1
    assert resultado[0].marca == "Fiat"
