from Usuario import Usuario
from Reserva import Reserva

class General(Usuario):

    def __init__(self, nombre: str, apellido: str, documento: int, correo: str, contraseña: str):
        super().__init__(nombre, apellido, documento, correo, contraseña)
        self.historial_reservas: [Reserva] = []

    def gestionar_reserva(self):
        pass

    def gestionar_comentario(self):
        pass
