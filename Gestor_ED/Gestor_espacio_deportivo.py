from Espacio_deportivo import EspacioDeportivo
from Almacen_info import AlmacenInfo

class GestorED:
    @classmethod
    def agregar_espacio_deportivo(cls, id_espacio: int, nombre: str, reglamento: str, capacidad: int, db):
        espacio = EspacioDeportivo(id_espacio, nombre, reglamento, capacidad)
        db.registrar_espacio_deportivo(espacio)

    @classmethod
    def eliminar_espacio_deportivo(cls, id_espacio: int, db):
        for espacio in AlmacenInfo.EspaciosDeportivos:
            if espacio.id == id_espacio:
                db.eliminar_espacio_deportivo(espacio)
