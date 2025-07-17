import socket
import json

HOST = 'localhost'
PORT = 9090


def filters_results(filters: dict):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(json.dumps(filters).encode())

        chunks = []
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            chunks.append(chunk)

        data = b"".join(chunks)

    return json.loads(data.decode())
