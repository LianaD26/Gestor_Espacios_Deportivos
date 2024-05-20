class Usuario:
    def __init__(self, nombre: str, apellido: str, documento: int, correo: str, contraseña: str):
        self.nombre: str = nombre
        self.apellido: str = apellido
        self.documento: int = documento
        self.correo: str = correo
        self.contraseña: str = contraseña
