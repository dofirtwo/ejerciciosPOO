class Carro():
    def __init__(self,placa,marca,modelo,color):
        self.__placa=placa
        self.marca=marca
        self.__modelo=modelo 
        self.color=color
        
    def getPlaca(self):
        return self.__placa
    def getModelo(self):
        return self.__modelo
    
    def setPlaca(self,placa):
        self.__placa=placa
    def setModelo(self,modelo):
        self.__modelo=modelo

class Libro():
    def __init__(self,titulo,autor,numeroPaginas):
       self.__titulo=titulo
       self.__autor=autor
       self.__numeroPaginas=numeroPaginas
    
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getNumeroPaginas(self):
        return self.__numeroPaginas
    
    def setTitulo(self,titulo):
        self.__titulo=titulo
    def setAutor(self,autor):
        self.__autor=autor
    def setNumeroPaginas(self,numeroPaginas):
        self.__numeroPaginas=numeroPaginas

carro= Carro("xxx111","Toyota",2015,"Azul")
print(f"su carro de placa {carro.getPlaca()} es modelo {carro.getModelo()}")
libro= Libro("La Llamada de Cthulhu","H.P LoveCraft",96)
print(f"el libro {libro.getTitulo()} escrito por {libro.getAutor()} tiene {libro.getNumeroPaginas()} paginas")
    