from pasajero import Pasajero
class Vuelo():
    def __init__(self,numeroDeVuelo,fecha,ciudadOrigen,ciudadDestino):
        self.__numeroDeVuelo=numeroDeVuelo
        self.__fecha=fecha
        self.__ciudadOrigen=ciudadOrigen
        self.__ciudadDesino=ciudadDestino
        self.__listadoPasajeros=[]
    
    def getNumeroDeVuelo(self):
        return self.__numeroDeVuelo
    def getFecha(self):
        return self.__fecha
    def getCiudadOrigen(self):
        return self.__ciudadOrigen
    def getCiudadDestino(self):
        return self.__ciudadDesino
    def getListaPasajeros(self):
        return self.__listadoPasajeros
    
    def setNumeroDeVuelo(self,numeroDeVuelo):
        self.__numeroDeVuelo=numeroDeVuelo
    def setFecha(self,fecha):
        self.__fecha=fecha
    def setCiudadOrigen(self,ciudadOrigen):
        self.__ciudadOrigen=ciudadOrigen
    def setCiudadDestino(self,ciudadDestino):
        self.__ciudadDesino=ciudadDestino
    
    def AgregarPasajero(self,nombre,id,correo):
        if(nombre and id and correo):
            pasajero=Pasajero(nombre,id,correo)
            self.__listadoPasajeros.append(pasajero)
        else:
            return False