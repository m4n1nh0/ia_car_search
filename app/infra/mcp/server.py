import socket
import json
from app.infra.db.database import SessionLocal
from app.infra.db.car_persistence import CarPersistence
from app.domain.rules.car_rule import CarRule

HOST = 'localhost'
PORT = 9090


def start_server():
    db = SessionLocal()
    car_persistence = CarPersistence(db)
    car_rule = CarRule(car_persistence)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor MCP ouvindo em {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Conectado por {addr}")
                data = conn.recv(4096)
                if not data:
                    continue

                try:
                    filtros = json.loads(data.decode())
                    resultado = car_rule.buscar_veiculos_filtrados(filtros)
                    resposta = [r.__dict__ for r in resultado]
                    for r in resposta:
                        r.pop('_sa_instance_state', None)

                    json_data = json.dumps(resposta).encode()
                    conn.sendall(json_data)
                except Exception as e:
                    error = {"erro": str(e)}
                    conn.sendall(json.dumps(error).encode())


if __name__ == "__main__":
    start_server()
