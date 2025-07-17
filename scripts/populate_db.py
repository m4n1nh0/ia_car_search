from faker import Faker
import random
from app.infra.db.car_model import CarModel
from app.infra.db.database import SessionLocal, Base, engine

def start_populate():
    fake = Faker()
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    carrocerias = ["SUV", "Sedã", "Hatch", "Pickup"]
    cores = ["Preto", "Branco", "Prata", "Vermelho", "Azul"]
    transmissoes = ["Manual", "Automática"]
    combustiveis = ["Gasolina", "Álcool", "Flex", "Diesel"]
    marcas = [
        "Fiat", "Volkswagen", "Chevrolet", "Ford", "Toyota", "Hyundai",
        "Honda", "Nissan", "Renault", "Jeep", "Peugeot", "Kia", "Citroën"
    ]

    for _ in range(100):
        carro = CarModel(
            marca=random.choice(marcas),
            modelo=fake.word().capitalize(),
            ano=random.randint(2005, 2023),
            combustivel=random.choice(combustiveis),
            motorizacao=random.choice(["1.0", "1.6", "2.0"]),
            quilometragem=random.randint(0, 150000),
            portas=random.choice([2, 4]),
            transmissao=random.choice(transmissoes),
            cor=random.choice(cores),
            preco=round(random.uniform(20000, 120000), 2),
            tipo_carroceria=random.choice(carrocerias),
            placa=fake.license_plate(),
            revisao=fake.date_this_decade().isoformat()
        )
        db.add(carro)

    db.commit()
    print("Banco populado com 100 carros fictícios de marcas reais.")


if __name__ == "__main__":
    start_populate()
