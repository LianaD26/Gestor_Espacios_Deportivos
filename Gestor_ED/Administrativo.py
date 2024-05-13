from Usuario import Usuario


class Administrativo(Usuario):
    def __init__(self, documento: int, nombre: str, apellido: str, correo: str, contraseña: str):
        super().__init__(nombre, apellido, documento, correo, contraseña)

    def crear_espacio_deportivo(self):
        pass

    def registrar_instructor(self):
        pass

    def registrar_equipamiento(self):
        pass
