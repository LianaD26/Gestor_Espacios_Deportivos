from Reseña import Reseña

class EspacioDeportivo:

    def __init__(self, id: int, nombre: str, reglamento: str, capacidad: int):
        self.id: int = id
        self.nombre: str = nombre
        self.reglamento: str = reglamento
        self.capacidad: int = capacidad
        self.historial_reseñas: [Reseña] = []
