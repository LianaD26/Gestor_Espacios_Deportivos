from Usuario import Usuario
from Espacio_deportivo import EspacioDeportivo


class Instructor(Usuario):

    def __init__(self, nombre: str, apellido: str, documento: int, correo: str, contraseña: str,
                 espacio_deportivo: EspacioDeportivo):

        super().__init__(nombre, apellido, documento, correo, contraseña)
        self.espacio_deportivo: EspacioDeportivo = espacio_deportivo
