sql_select_vehicles = "SELECT * FROM taller.vehicle;"

sql_select_vehicle = "SELECT * FROM taller.vehicle WHERE id = %s;"

sql_insert_motor = """
INSERT INTO taller.motor (cc, cv, peso)
VALUES (%s, %s, %s)
"""

sql_insert_vehicle = """
INSERT INTO taller.vehicle (fabricante, modelo, color, id_motor)
VALUES (%s, %s, %s, %s)
"""

sql_update_vehicle = """
UPDATE taller.vehicle
SET fabricante = %s, modelo = %s, color = %s
WHERE id = %s;
"""

sql_delete_vehicle = """
DELETE FROM taller.vehicle
WHERE id = %s;
"""

sql_delete_vehicles = """
TRUNCATE TABLE taller.vehicle;
"""