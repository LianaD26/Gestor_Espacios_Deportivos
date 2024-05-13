from DB import DB
from Administrativo import Administrativo

class GestorInicioSesion:
    @classmethod
    def iniciar_sesion_administrativo(cls):
        print("Iniciar sesión como administrativo...")

    @classmethod
    def iniciar_sesion_general(cls):
        print("Iniciar sesión como general...")

    @classmethod
    def registrar_administrativo(cls, documento: int, nombre: str, apellido: str, correo: str, contraseña: str, db):
        print("Registrarse como administrativo...")
        print(documento, nombre, apellido, correo, contraseña)
        admin = Administrativo(documento, nombre, apellido, correo, contraseña)
        #db = DB(host="localhost", user="User1", password="passw2024", database="GestorED")
        db.registrar_administrativo(admin)

    @classmethod
    def registrar_general(cls):
        print("Registrarse como general...")

    # si inicia sesión que ese usuario exista en la base de datos
    def verificar_administrativo(self):
        pass

    def verificar_general(self):
        pass

