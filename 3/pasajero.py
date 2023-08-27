class Pasajero():
    def __init__(self,nombre,identificacion,correo):
        self.__nombre=nombre
        self.__identificacion=identificacion
        self.__correo=correo
    
    def getNombre(self):
        return self.__nombre
    def getIdentificacion(self):
        return self.__identificacion
    def getCorreo(self):
        return self.__correo
    
    def setNombre(self,nombre):
        self.__nombre=nombre
    def setIdentificacion(self,identificacion):
        self.__identificacion=identificacion
    def setCorreo(self,correo):
        self.__correo=correo