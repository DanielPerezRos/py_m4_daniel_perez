"""
leer de terminal datos y almacenarlos - CRUD
"""
from crud import *

init_schema() # Crea el esquema y tablas de la db
load_data() # Carga datos de prueba en la db

while True:
    print(
    """
    1 - Consultar vehículos
    2-  Consultar vehículo por id
    3-  Crear nuevo vehículo
    4 - Editar vehículo
    5 - Borrar vehículo por id
    6 - Borrar todos los vehículos
    7 - Salir
    """
    )
    option = int(input("Introduce una opción: "))
    if option == 1: #1 - Consultar vehículos
        vehicles = find_all()
        print("Listado de vehículos en base de datos: ")
        print(vehicles)

    if option == 2: # Consultar vehículo por id
        id_vehicle = int(input("Introduce el id de vehículo: "))
        vehicle = find_one(id_vehicle)
        if vehicle is not None:
            print("El vehículo encontrado es: ")
            print(vehicle)
        else:
            print("El vehículo solicitado no existe")
    if option == 3:
        vehicle = input_new_vehicle()
        check = create(vehicle)
        if check:
            print("vehículo creado correctamente")

    if option == 4:
        vehicle = input_update_vehicle()
        check = update(vehicle)
        if check:
            print("vehículo editado correctamente")

    if option == 5:
        id_vehicle = int(input("Introduce el id del vehículo: "))
        check = delete_one(id_vehicle)
        if check:
            print("Vehículo borrado correctamente")

    if option == 6:
        check = delete_all()
        if check:
            print("vehículos borrados correctamente")

    if option == 7:
        break;

print("Hasta la próxima")