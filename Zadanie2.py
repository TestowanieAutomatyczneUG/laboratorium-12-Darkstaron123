class Subscriber:
    def __init__(self):
        self.clients = []

    def addClient(self, id, client):
        self.clients.append({'id': id, 'client': client})
        return self.clients

    def deleteClient(self, id):
        for i in self.clients:
            if i['id'] == id:
                self.clients.remove(i)
                return self.clients
        raise Exception('brak')

    def sendMsg(self, id, msg):
        pass