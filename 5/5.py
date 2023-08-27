from cliente import Cliente
from venta import Venta
from producto import Producto
from tienda import Tienda
from datetime import datetime

tienda = Tienda("TiendaADSO")

producto1 = Producto(1234,"leche",5000)
tienda.crearProducto(producto1)
producto2 = Producto(4567,"pan",3000)
tienda.crearProducto(producto2)

cliente = Cliente("pedro","carrera 21 #4-44","edro123@gmail.com")
tienda.crearCliente(cliente)

venta= Venta(datetime.now(),cliente)
tienda.crearVenta(venta)
venta.agregarDetalleCliente(producto1,5)
venta.agregarDetalleCliente(producto2,10)

for c in tienda.getListaCliente():
    print(f"nombre: {c.getNombre()}, direccion: {c.getDireccion()}, correo: {c.getCorreo()}")
for p in tienda.getListaProducto():
    print(f"codigo: {p.getCodigo()}, nombre: {p.getNombre()}, precio: {p.getPrecio()}")
suma=0
for v in tienda.getListaVenta():
    for d in v.getListaDetalle():
        print(f"fecha: {v.getFecha()}, cliente: {v.getCliente().getNombre()}, Precio Unitario: {d.getProducto().getPrecio()}, cantidad: {d.getCantidad()}, Valor Total: {d.getValor()}")
        valor=d.getValor()
        suma=valor+suma

print(f"el total de las Ventas es: {suma}")
