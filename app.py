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
        if vehicles != []:
            print("Listado de vehículos en base de datos: ")
            print(vehicles)
        else:
            print("No hay vehículos en la BBDD")

    if option == 2: # Consultar vehículo por id
        id_vehicle = int(input("Introduce el id de vehículo: "))
        vehicle = find_one(id_vehicle)
        if vehicle is not None:
            print("El vehículo encontrado es: ")
            print(vehicle)
        else:
            print("El vehículo solicitado no existe")
    if option == 3: # Crear nuevo vehículo
        vehicle = input_new_vehicle()
        check = create(vehicle)
        if check:
            print("Vehículo creado correctamente")

    if option == 4:
        vehicle = input_update_vehicle()
        check = update(vehicle)
        if check:
            print("Vehículo editado correctamente")

    if option == 5:
        id_vehicle = int(input("Introduce el id del vehículo: "))
        check = delete_one(id_vehicle)
        if check:
            print("Vehículo borrado correctamente")

    if option == 6:
        print("Esto borrará todos los vehículos de la base de datos.")
        confirm = bool(int(input("¿Está seguro de que quiere borrar todos? (1 Sí, 0 No)")))
        if not confirm:
            continue

        delete_all()
        print("Usuarios borrados correctamente")

    if option == 7:
        break;

print("¡Hasta la próxima!")