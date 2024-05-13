from Usuario import Usuario

class General(Usuario):

    def __init__(self, documento: int, nombre: str, apellido: str, correo: str, contraseña: str):
        super().__init__(nombre, apellido, documento, correo, contraseña)

    def gestionar_reserva(self):
        pass

    def gestionar_comentario(self):
        pass
