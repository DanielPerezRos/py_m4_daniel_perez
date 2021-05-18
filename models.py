class Vehicle:
    def __init__(self, id, fabricante, modelo, color, motor):
        self.id = id
        self.fabricante = fabricante
        self.modelo = modelo
        self.color = color
        self.motor = motor

    def __str__(self):
        return f"Vehicle(id={self.id}, " \
               f"fabricante = {self.fabricante}, " \
               f"modelo = {self.modelo}, " \
               f"color = {self.color}, " \
               f"motor = {self.motor} " \
               f")"

    def __repr__(self):
        return self.__str__()


class Motor:
    def __init__(self, id_motor, cc, cv, peso):
        self.id_motor = id_motor
        self.cc = cc
        self.cv = cv
        self.peso = peso

    def __str__(self):
        return f"Motor(id_motor={self.id_motor}, " \
               f"cc = {self.cc}, " \
               f"cv = {self.cv}, " \
               f"peso = {self.peso} " \
               f")"

    def __repr__(self):
        return self.__str__()