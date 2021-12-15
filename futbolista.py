from deportista import Deportista
from persona import Persona


class Futbolista(Persona,Deportista):

    _listaFutbolistas=[]
    def __init__(self,nombre,edad,altura,sexo,años,goles,rojas,pierna):
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,"Futbol",años)
        self._golesMarcados=goles
        self._tarjetasRojas=rojas
        self._piernaHabil=pierna
        Futbolista.listaFutbolistas.append(self)

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
        return ("Mi nombre es "+self.getNombre()+" soy profesional en el deporte "+self.getDeporte()+" Tengo"+str(self.getEdad())+" años de edad y llevo "+str(self.getAñosPracticando())+" años en el deporte")