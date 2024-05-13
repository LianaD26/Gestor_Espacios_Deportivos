from Almacen_info import AlmacenInfo

class GestorReserva:
    @classmethod
    def mostrar_espacios_deportivo(cls):
        espacios = []
        # id_espacio, nombre, reglamento, capacidad
        for ed in AlmacenInfo.EspaciosDeportivos:
            e = {"Id": ed.id, "Nombre": ed.nombre, "Reglamento": ed.reglamento, "Capacidad": ed.capacidad}
            espacios.append(e)
        return espacios

    @classmethod
    def agendar_espacio_deportivo(cls):
        pass

    @classmethod
    def mostrar_instructores(cls):
        instructores = []
        for ed in AlmacenInfo.Instructores:
            e = {"Documento": ed.documento, "Nombre": ed.nombre, "Apellido": ed.apellido, "Correo": ed.correo, "Contraseña": ed.contraseña}
            instructores.append(e)
        return instructores

    @classmethod
    def agendar_instructor(cls):
        pass

    @classmethod
    def mostrar_equipamiento(cls):
        pass

    @classmethod
    def agendar_equipamiento(cls):
        pass