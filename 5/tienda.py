from cliente import Cliente
from venta import Venta
from producto import Producto
class Tienda():
    def __init__(self, nombre):
        self.__nombre=nombre
        self.__listaCliente=[]
        self.__listaVenta=[]
        self.__listaProducto=[]
 
    def getNombre(self):
        return self.__nombre
    def getListaCliente(self):
        return self.__listaCliente
    def getListaVenta(self):
        return self.__listaVenta
    def getListaProducto(self):
        return self.__listaProducto
    
    def crearCliente(self, cliente):
        self.__listaCliente.append(cliente)
        
    def crearProducto(self, producto):
        self.__listaProducto.append(producto)
        
    def crearVenta(self, venta):
        self.__listaVenta.append(venta)