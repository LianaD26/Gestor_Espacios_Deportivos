from Usuario import Usuario
from Espacio_deportivo import EspacioDeportivo


class Instructor(Usuario):
    def __init__(self, documento: int, nombre: str, apellido: str, correo: str, contraseña: str,
                 espacio_deportivo: str):

        super().__init__(nombre, apellido, documento, correo, contraseña)
