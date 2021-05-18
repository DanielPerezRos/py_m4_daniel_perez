# Aplicación CRUD, que lea datos de vehículos por consola y los almacene en base datos MySQL utilizando objetos. La aplicación ofrece las siguientes opciones:

1 – Consultar vehículos: devuelve los vehículos que tiene guardados en una estructura de datos.

2 – Consultar un vehículo: solicita el id del vehículo y en base a eso mostrar los datos de ese vehículo y del motor asociado.

3 – Crear un nuevo vehículo: pide los datos de un vehículo (id, fabricante, modelo, ....) Importante: crear también un objeto Motor y asociarlo.

4 – Editar un vehículo: pide el id del vehículo y después todos los datos para sobreescribir los que ya tenía para ese vehículo. Importante tener el cuenta pedir los datos del motor

5 – Borrar un vehículo: pide el id del vehículo y lo borra de la estructura de datos.

6 - Borrar todos: vaciar la estructura de datos de vehículos. Se pierden los vehículos.

7 – Salir: rompe el bucle y termina la aplicación.

Todas las operaciones anteriores se harán en una base de datos llamada taller. Crear las tablas correspondientes.

Asociación 1:1 entre Vehículo y Motor.

Con un bucle se pide al usuario que introduzca una opción (por el número de opción) y en base a la opción se realiza una operación o se preguntan más datos para poder llevar a cabo la acción elegida. 
Se imprime en terminal los resultados de la acción solicitada.