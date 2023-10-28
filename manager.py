from flat import Flat
from client import Client

class Manager:
    def __init__(self):
        self._flats :list[Flat] = []
        self._clients :list[Client]= []

    def newFlat(self, code, area):
        flat = Flat(code, area)
        self._flats.append(flat)
        return flat

    def getCode(self, flat: Flat):
        return flat.getCode()

    def getDimention(self, flat: Flat):
        return flat.getDimention()

    def setTariffs(self, flat :Flat, tariffs):
        flat.setTariffs(tariffs)

    def getTariffs(self, flat : Flat):
        return flat.getTariffs()
    
    def newClient(self, first_name, last_name, id):
        client = Client(first_name, last_name, id)
        self._clients.append(client)
        return client

    def getClient(self, client_id):
        for client in self._clients:
            if client.getID() == client_id:
                return client
        return 'bunday idli klient mavjud emas'

    def getClients(self):
        return self._clients
    
    