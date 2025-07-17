from app.infra.db.car_model import CarModel


class CarPersistence:
    def __init__(self, db_session):
        self.db = db_session

    def buscar_por_filtros(self, limit: int = 5, **filtros):
        query = self.db.query(CarModel)

        for campo, valor in filtros.items():
            if hasattr(CarModel, campo):
                query = query.filter(getattr(CarModel, campo) == valor)

        return query.limit(limit).all()
