class Client:
    def __init__(self, first_name, last_name, id):
        self._first_name = first_name
        self._last_name = last_name
        self._id = id

    def getName(self):
        return self._first_name

    def getSurname(self):
        return self._last_name

    def getID(self):
        return self._id