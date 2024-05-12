from Usuario import Usuario


class Administrativo(Usuario):
    def __init__(self, nombre: str, apellido: str, documento: int, correo: str, contraseña: str):
        super().__init__(nombre, apellido, documento, correo, contraseña)

    def crear_espacio_deportivo(self):
        pass

    def registrar_instructor(self):
        pass

    def registrar_equipamiento(self):
        pass
