from Usuario import Usuario


class Administrativo(Usuario):
    def __init__(self, documento: int, nombre: str, apellido: str, correo: str, contraseña: str):
        super().__init__(nombre, apellido, documento, correo, contraseña)
