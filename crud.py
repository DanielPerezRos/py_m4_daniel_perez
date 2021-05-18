"""
Funciones CRUD
"""
# 1 importar el driver
import mysql.connector as con
from sql import *
from models import Vehicle, Motor

# 2 crear conexion a BD
database = con.connect(host="127.0.0.1", port="3306", user="root", password="admin")


def init_schema():
    database = con.connect(host="127.0.0.1", port="3306", user="root", password="admin")
    cursor = database.cursor()
    file = open("schema.sql")
    sql_content = file.read()
    file.close()
    sql_content = sql_content.replace("\n", "").replace("\t", "")
    sql_sentences = sql_content.split(";")

    for sql in sql_sentences:
        if len(sql) != 0:
            cursor.execute(sql + ";")

    cursor.close()
    database.close()

def init_schema_execute_multi():
    database = con.connect(host="127.0.0.1", port="3306", user="root", password="admin")
    cursor = database.cursor()
    file = open("schema.sql")
    sql_content = file.read()
    file.close()
    cursor.execute(sql_content)
    cursor.close()
    database.close()

def load_data():
    cursor = database.cursor()
    file = open("data.sql")
    sql_content = file.read()
    file.close()
    sql_content = sql_content.replace("\n", "").replace("\t", "")
    sql_sentences = sql_content.split(";")

    for sql in sql_sentences:
        if sql:
            cursor.execute(sql + ";")
            database.commit()

    cursor.close()
    database.close()

def find_all():
    database = con.connect(host="127.0.0.1", port="3306", user="root", password="admin", database="python_mysql")
    cursor = database.cursor()

    cursor.execute(sql_select_vehicles)

    results = cursor.fetchall()

    vehicles = []
    for result in results:
        if result[4] is not None:
            motor = Motor(result[4], None, None, None)

        else:
            motor = None
        vehicle = Vehicle(result[0], result[1], result[2], result[3], motor)
        vehicles.append(vehicle)

    cursor.close()
    database.close()
    return vehicles

def find_one(id_vehicle):
    database = con.connect(host="127.0.0.1", port="3306", user="root", password="admin", database="python_mysql")
    cursor = database.cursor()

    params = (id_vehicle,)
    cursor.execute(sql_select_vehicle, params)

    result = cursor.fetchone()
    cursor.close()
    database.close()

    if result[4] is not None:
        motor = Motor(result[4], None, None, None)
    else:
        motor = None
    vehicle = Vehicle(result[0], result[1], result[2], result[3], motor)

    return vehicle

def input_new_vehicle():

    print("Introduzca los datos del nuevo vehículo: ")
    fabricante = print("Introduce Fabricante: ")
    modelo = print("Introduce modelo: ")
    color = print("Introduce color: ")

    has_motor = bool(input("¿Tiene motor? (0- no, 1 - si"))
    if has_motor:
        fabricante = input("introduce el fabricante: ")
        modelo = input("introduce el Modelo: ")
        color = input("introduce la RAM")
        motor = Motor(None, fabricante, modelo, color)
    else:
        motor = None

    return Vehicle(None, fabricante, modelo, color, motor)


    fabricante = print("Introduce Fabricante: ")

def create_motor(motor):
    if motor is None:
        return -1
    database = con.connect(host="127.0.0.1", port="3306", user="root", password="admin", database="python_mysql")
    cursor = database.cursor()

    if vehicle.motor is not None:
        params = (
            vehicle.motor.manufacturer,
            vehicle.motor.model,
            vehicle.motor.ram,
        )
        cursor.execute(sql_insert_motor, params)
        vehicle.motor.id = cursor.lastrowid

def create(vehicle):
    if vehicle is None:
        return False
    database = con.connect(host="127.0.0.1", port="3306", user="root", password="admin", database="python_mysql")
    cursor = database.cursor()

    id_motor = create_motor(vehicle.motor)

    # Insertar usuario
    params = (
        vehicle.first_name,
        vehicle.last_name,
        vehicle.age,
       id_motor
    )
    cursor.execute(sql_insert_vehicle, params)
    database.commit()
    result_num = cursor.rowcount

    cursor.close()
    database.close()

    return False if result_num == 0 else True



def input_update_vehicle():
    pass

def update(vehicle):
    pass

def delete_one(id_vehicle):
    pass

def delete_all():
    pass