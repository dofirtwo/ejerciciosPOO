from producto import Producto
class DetalleVenta():
    def __init__(self, producto, cantidad, valor):
        self.__producto=producto
        self.__cantidad=cantidad
        self.__valor=valor
    
    def getProducto(self):
        return self.__producto
    def getCantidad(self):
        return self.__cantidad
    def getValor(self):
        return self.__valor
    
    def setProducto(self, producto):
        self.__producto=producto
    def setCantidad(self, cantidad):
        self.__cantidad=cantidad
    def setValor(self, valor):
        self.__valor=valor