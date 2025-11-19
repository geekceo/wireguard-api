from fastapi import FastAPI

from app.repository import implimentation as repositiory_implimentation
from app.service import implimentation as service_implimentation

from app.models import clients 

app = FastAPI(root_path="/api/v2")

@app.get('/clients')
def get_clients():

    result = repositiory_implimentation.get_clients()

    return result

@app.put('/clients/off')
def client_turn_off(request: clients.ClientGlobal):

    result = repositiory_implimentation.turn_off_client(client_name=request.client_name)

    service_implimentation.restart_wg_daemon()

    return result

@app.put('/clients/on')
def client_turn_on(request: clients.ClientGlobal):

    result = repositiory_implimentation.turn_on_client(client_name=request.client_name)

    service_implimentation.restart_wg_daemon()

    return result

@app.get('/clients/{client_name}')
def get_client_status(client_name: str):

    result = repositiory_implimentation.check_client_status(client_name=client_name)

    return {
        "status": result
    }
