from DB import DB
from Administrativo import Administrativo
from Almacen_info import AlmacenInfo
from General import General

class GestorInicioSesion:

    @classmethod
    def registrar_administrativo(cls, documento: int, nombre: str, apellido: str, correo: str, contraseña: str, db):
        admin = Administrativo(documento, nombre, apellido, correo, contraseña)
        AlmacenInfo.Administrativos.append(admin)
        db.registrar_administrativo(admin)

    @classmethod
    def registrar_general(cls, documento: int, nombre: str, apellido: str, correo: str, contraseña: str, db):
        print("Registrarse como general...")
        general = General(documento, nombre, apellido, correo, contraseña)
        AlmacenInfo.Generales.append(general)
        db.registrar_general(general)

    @classmethod
    def iniciar_sesion_administrativo(cls, documento: int, ctr: str):
        for i in AlmacenInfo.Administrativos:
            if i.documento == documento and i.contraseña == ctr:
                return True
        return False

    @classmethod
    def iniciar_sesion_general(cls, documento: int, ctr: str):
        for i in AlmacenInfo.Generales:
            if i.documento == documento and i.contraseña == ctr:
                return True
        return False

