from deportista import Deportista
from persona import Persona

class Futbolista(Deportista):

    _listaFutbolistas=[]
    def __init__(self,nombre,edad,altura,sexo,años,goles,rojas,pierna):
        super().__init__(nombre,edad,altura,sexo,"Futbol",años)
        self._golesMarcados=goles
        self._tarjetasRojas=rojas
        self._piernaHabil=pierna
        Futbolista._listaFutbolistas.append(self)

    @classmethod
    def getListaFutbolistas(cls):
        cls._listaFutbolistas

    def getGolesMarcados(self):
        return self._golesMarcados
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def getPiernaHabil(self):
        return self._piernaHabil

    def setGolesMarcados(self,nuevo):
        self._golesMarcados=nuevo

    def setTarjetasRojas(self,nuevo):
        self._tarjetasRojas=nuevo
    
    def setPiernaHabil(self,nuevo):
        self._piernaHabil=nuevo

    @classmethod
    def setListaFutbolistas(cls,nuevo):
        cls._listaFutbolistas=nuevo

    def __str__(self):
        return "Mi nombre es {} soy profesional en el deporte {} Tengo {} años de edad y llevo {} años en el deporte".format(self.getNombre(), self.getDeporte(), str(self.getEdad()), str(self.getAñosPracticando()))
    