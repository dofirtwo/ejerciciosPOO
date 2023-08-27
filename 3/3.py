from pasajero import Pasajero
from vuelo import Vuelo
from empresa import Empresa

e=Empresa("Avianca")

def crearVuelo():
    verificacio=False
    numeroVuelo=int(input("Ingrese el numero de Vuelo: "))
    for v in e.getListaVuelos():
        if numeroVuelo==v.getNumeroDeVuelo():
            verificacio=True
            break
    if verificacio==False:
        fecha = input("Ingrese la fecha (dd-mm-yyyy)")
        ciudadOrigen=input("Ingrese la ciudad de Origen: ")
        ciudadDestino=input("Ingrese la ciudad de Destino: ")
        e.CrearVuelo(numeroVuelo,fecha,ciudadOrigen,ciudadDestino)
        print("vuelo creado correctamente")
    else:
        print("el vuelo con ese numero ya existe")

def listarVuelo():
    for v in e.getListaVuelos():
        print("------------------------------------------------------")
        print(f"El numero de vuelo es: {v.getNumeroDeVuelo()}")
        print(f"la fecha del vuelo es: {v.getFecha()}")
        print(f"la ciudad origen de vuelo es: {v.getCiudadOrigen()}")
        print(f"la ciudad destino de vuelo es: {v.getCiudadDestino()}")
        print()
   
def registrarPasajero():
    verificacion=False
    numeroVuelo=int(input("Ingrese el numero de Vuelo para agregar: "))
    for v in e.getListaVuelos():
        if numeroVuelo==v.getNumeroDeVuelo():
            nombre=input("Ingrese nombre: ")
            indentificacion=int(input("Ingrese la identificacion: "))
            correo=input("Ingrese el correo: ")
            v.AgregarPasajero(nombre,indentificacion,correo)
            verificacion=True
            break
    if verificacion==False:
        print(f"el Numero de vuelo {numeroVuelo} NO EXISTE")
    else:
        print("Pasajero agregado correctamente")
        
def listarPasajeros():
    numeroVuelo=int(input("Ingrese el numero de Vuelo para agregar: "))
    for v in e.getListaVuelos():
        if numeroVuelo==v.getNumeroDeVuelo():
            
            for p in v.getListaPasajeros():
                print("-------------------------------------------------------")
                print(f"Nombre: {p.getNombre()}")
                print(f"Identificacion: {p.getIdentificacion()}")
                print(f"Correo: {p.getCorreo()}")
                print()
                break
x=0
while x!=5:
    print("1. Crear Vuelo")
    print("2. Agregar Pasajeros")
    print("3. Listar Vuelos")
    print("4. Listar Pasajeros")
    print("5. Salir")
    x=int(input("Ingrese Opción (1-5): "))
    if x==1:
        crearVuelo()
    if x==2:
        registrarPasajero()
    if x==3:
        listarVuelo()
    if x==4:
        listarPasajeros()
