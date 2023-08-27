from vuelo import Vuelo
class Empresa():
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__listaVuelos=[]
        
    def getNombre(self):
        return self.__nombre
    def getListaVuelos(self):
        return self.__listaVuelos
    
    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def CrearVuelo(self,numero=None,fecha=None,ciudadOrigen=None,ciudadDestino=None,):
        if (numero and fecha and ciudadOrigen and ciudadDestino):
            vuelo=Vuelo(numero,fecha,ciudadOrigen,ciudadDestino)
            self.__listaVuelos.append(vuelo)
        else:
            return False