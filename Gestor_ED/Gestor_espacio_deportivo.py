from Espacio_deportivo import EspacioDeportivo

class GestorED:
    @classmethod
    def agregar_espacio_deportivo(cls, id_espacio: int, nombre: str, reglamento: str, capacidad: int, db):
        espacio = EspacioDeportivo(id_espacio, nombre, reglamento, capacidad)
        db.registrar_espacio_deportivo(espacio)
