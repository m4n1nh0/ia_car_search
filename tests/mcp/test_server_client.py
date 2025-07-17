import multiprocessing
import time

from app.infra.mcp.client import filters_results
from app.infra.mcp.server import start_server


def run_server_process():
    start_server()


def test_mcp_client_server_interaction():
    server = multiprocessing.Process(target=run_server_process)
    server.start()
    time.sleep(1)

    try:
        filtros = {"marca": "Toyota"}
        resposta = filters_results(filtros)

        assert isinstance(resposta, list)
        if resposta:
            assert "marca" in resposta[0]
            assert resposta[0]["marca"] == "Toyota"
    finally:
        server.terminate()
        server.join()
