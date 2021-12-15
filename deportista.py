from persona import Persona


class Deportista:
    def __init__(self,nombre,edad,altura,sexo,deporte,años):
        Persona().__init__(nombre,edad,altura,sexo)
        self._deporte=deporte
        self._añosPracticando=años

    
    def getDeporte(self):
        return self._deporte
    
    def getAñosPracticando(self):
        return self._añosPracticando

    def setDeporte(self,nuevo):
        self._deporte=nuevo

    def setAñosPracticando(self,nuevo):
        self._añosPracticando=nuevo