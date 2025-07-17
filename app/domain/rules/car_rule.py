from typing import List
from app.domain.dto.car_dto import CarDTO
from app.utils.utilities import normalizar_marca


class CarRule:
    def __init__(self, persistence):
        self.persistence = persistence

    def buscar_veiculos_filtrados(self, filtros: dict, limit: int = 5) -> List[CarDTO]:
        if "marca" in filtros:
            filtros["marca"] = normalizar_marca(filtros["marca"])
        carros = self.persistence.buscar_por_filtros(limit=limit, **filtros)
        return [CarDTO.model_validate(c) for c in carros]

