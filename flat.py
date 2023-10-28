class Flat:
    def __init__(self, kodi, maydoni) -> None:
        self._kodi = kodi
        self._maydoni = maydoni
        self._tarifs = []

    def getCode(self):
        return self._kodi
    
    def getDimention(self):
        return self._maydoni
    
    def setTariffs(self, tariffs):
        self.tariffs = tariffs

    def getTariffs(self):
        return self.tariffs
    