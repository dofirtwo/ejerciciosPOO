from cliente import Cliente
from detalleVenta import DetalleVenta
from producto import Producto
from datetime import datetime
class Venta():
    def __init__(self, fecha, cliente):
        self.__fecha=fecha
        self.__cliente=cliente
        self.__listaDetalle=[]
        
    def getFecha(self):
        return self.__fecha
    def getCliente(self):
        return self.__cliente
    def getListaDetalle(self):
        return self.__listaDetalle
    
    def setFecha(self, fecha):
        self.__fecha=fecha
    def setCliente(self, cliente):
        self.__cliente=cliente
    
    def agregarDetalleCliente(self, producto, cantidad):
        valor = producto.getPrecio()*cantidad
        detalleVenta= DetalleVenta(producto,cantidad,valor)
        self.__listaDetalle.append(detalleVenta)