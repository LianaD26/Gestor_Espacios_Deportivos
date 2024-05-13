import pymysql
from Administrativo import Administrativo
from General import General
from Almacen_info import AlmacenInfo
from Espacio_deportivo import EspacioDeportivo
from Instructor import Instructor
from Equipamiento import Equipamiento

class DB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def conectar(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            if self.connection.open:
                print("Conexión establecida correctamente")
                return True

        except pymysql.Error as error:
            print("Error al conectar a la base de datos:", error)
            return False

    def desconectar(self):
        if self.connection and self.connection.open:
            self.connection.close()
            print("Conexión cerrada")

    def registrar_administrativo(self, admin: Administrativo):
        # documento, nombre, apellido, correo, contraseña
        try:
            cursor = self.connection.cursor()

            sql = ("INSERT INTO Administrativos (documento, nombre, apellido, correo, contraseña) "
                   "VALUES (%s, %s, %s, %s, %s)")
            cursor.execute(sql, (admin.documento, admin.nombre, admin.apellido, admin.correo, admin.contraseña))

            self.connection.commit()

            print("Registro de administrativo creado exitosamente.")

        except pymysql.Error as error:
            print("Error al registrar administrativo:", error)

    def registrar_general(self, general: General):
        try:
            cursor = self.connection.cursor()

            sql = ("INSERT INTO Generales (documento, nombre, apellido, correo, contraseña) "
                   "VALUES (%s, %s, %s, %s, %s)")
            cursor.execute(sql, (general.documento, general.nombre, general.apellido, general.correo, general.contraseña))

            self.connection.commit()

            print("Registro de general creado exitosamente.")

        except pymysql.Error as error:
            print("Error al registrar general:", error)

    def registrar_espacio_deportivo(self, espacio_deportivo: EspacioDeportivo):
        try:
            cursor = self.connection.cursor()

            sql = ("INSERT INTO Espacios_deportivos (id_espacio, nombre, reglamento, capacidad) "
                   "VALUES (%s, %s, %s, %s)")
            cursor.execute(sql, (espacio_deportivo.id, espacio_deportivo.nombre, espacio_deportivo.reglamento,
                                 espacio_deportivo.capacidad))

            self.connection.commit()

            print("Registro de espacio deportivo creado exitosamente.")

        except pymysql.Error as error:
            print("Error al registrar espacio deportivo:", error)

    def eliminar_espacio_deportivo(self, espacio_deportivo: EspacioDeportivo):
        try:
            cursor = self.connection.cursor()

            sql = "DELETE FROM Espacios_deportivos WHERE id_espacio = %s"
            cursor.execute(sql, espacio_deportivo.id)

            self.connection.commit()

            print("Espacio deportivo eliminado exitosamente.")

        except pymysql.Error as error:
            print("Error al eliminar espacio deportivo:", error)

    def obtener_administrativos(self):
        try:
            cursor = self.connection.cursor()

            sql = "SELECT * FROM Administrativos"
            cursor.execute(sql)

            for row in cursor.fetchall():
                documento, nombre, apellido, correo, contrasena = row
                administrativo = Administrativo(documento, nombre, apellido, correo, contrasena)
                AlmacenInfo.Administrativos.append(administrativo)

        except pymysql.Error as error:
            print("Error al obtener administrativos:", error)

    def obtener_generales(self):
        try:
            cursor = self.connection.cursor()

            sql = "SELECT * FROM Generales"
            cursor.execute(sql)

            for row in cursor.fetchall():
                documento, nombre, apellido, correo, contrasena = row
                general = General(documento, nombre, apellido, correo, contrasena)
                AlmacenInfo.Generales.append(general)

        except pymysql.Error as error:
            print("Error al obtener generales:", error)

    def obtener_espacios_deportivos(self):
        try:
            cursor = self.connection.cursor()

            sql = "SELECT * FROM Espacios_deportivos"
            cursor.execute(sql)

            for row in cursor.fetchall():
                id_espacio, nombre, reglamento, capacidad = row
                espacio = EspacioDeportivo(id_espacio, nombre, reglamento, capacidad)
                AlmacenInfo.EspaciosDeportivos.append(espacio)

        except pymysql.Error as error:
            print("Error al obtener espacios deportivos:", error)

    def obtener_instructores(self):
        try:
            cursor = self.connection.cursor()

            sql = "SELECT * FROM Instructores"
            cursor.execute(sql)

            for row in cursor.fetchall():
                documento, nombre, apellido, correo, contraseña, espacio_deportivo = row
                instructor = Instructor(documento, nombre, apellido, correo, contraseña, espacio_deportivo)
                AlmacenInfo.Instructores.append(instructor)

        except pymysql.Error as error:
            print("Error al obtener instructores:", error)

    def obtener_equipamientos(self):
        try:
            cursor = self.connection.cursor()

            sql = "SELECT * FROM Equipamientos"
            cursor.execute(sql)

            for row in cursor.fetchall():
                id_equipo, nombre, cantidad = row
                equipamiento = Equipamiento(id_equipo, nombre, cantidad)
                AlmacenInfo.Equipamientos.append(equipamiento)

        except pymysql.Error as error:
            print("Error al obtener equipamientos:", error)

    def agendar_reserva_ED(self, id_general: int, id_espacio: int, hora_inicio: int, hora_fin: int):
        try:
            cursor = self.connection.cursor()

            sql = ("INSERT INTO Reservas_ED (id_reserva, hora_inicio, hora_fin) "
                   "VALUES (%s, %s, %s)")
            cursor.execute(sql, (id_espacio, hora_inicio, hora_fin))

            self.connection.commit()

            print("Espacio deportivo agendado exitosamente.")

            cursor_ = self.connection.cursor()

            sql_ = ("INSERT INTO Historial_reservas_ED (id_general, id_reserva) "
                   "VALUES (%s, %s)")
            cursor_.execute(sql_, (id_general, id_espacio))

            self.connection.commit()

        except pymysql.Error as error:
            print("Error al agendar espacio deportivo:", error)

    def agendar_reserva_instructor(self, id_general: int, id_instructor: int, hora_inicio: int, hora_fin: int):
        try:
            cursor = self.connection.cursor()

            sql = ("INSERT INTO Reservas_instructor (id_reserva, hora_inicio, hora_fin) "
                   "VALUES (%s, %s, %s)")
            cursor.execute(sql, (id_instructor, hora_inicio, hora_fin))

            self.connection.commit()

            print("Instructor agendado exitosamente.")

            cursor_ = self.connection.cursor()

            sql_ = ("INSERT INTO Historial_reservas_instructor (id_general, id_reserva) "
                   "VALUES (%s, %s)")
            cursor_.execute(sql_, (id_general, id_instructor))

            self.connection.commit()

        except pymysql.Error as error:
            print("Error al agendar instructor:", error)

    def agendar_reserva_equipamiento(self, id_general: int, id_equipamiento: int, hora_inicio: int, hora_fin: int):
        try:
            cursor = self.connection.cursor()

            sql = ("INSERT INTO Reservas_equipamiento (id_reserva, hora_inicio, hora_fin) "
                   "VALUES (%s, %s, %s)")
            cursor.execute(sql, (id_equipamiento, hora_inicio, hora_fin))

            self.connection.commit()

            print("Equipamiento agendado exitosamente.")

            cursor_ = self.connection.cursor()

            sql_ = ("INSERT INTO Historial_reservas_equipamiento (id_general, id_reserva) "
                   "VALUES (%s, %s)")
            cursor_.execute(sql_, (id_general, id_equipamiento))

            self.connection.commit()

        except pymysql.Error as error:
            print("Error al agendar equipamiento:", error)

    def mostrar_reservas_general(self, id_general: int):
        reservas = []
        try:
            # reservas de ED
            cursor = self.connection.cursor()

            sql = "select * from Historial_reservas_ED where id_general = %s;"
            cursor.execute(sql, (id_general,))

            for row in cursor.fetchall():
                id_general, id_reserva = row
                reserva = {"id_reserva": id_reserva, "tipo": "Espacio deportivo"}
                reservas.append(reserva)

            # reservas de instructores
            cursor2 = self.connection.cursor()

            sql2 = "select * from Historial_reservas_instructor where id_general = %s;"
            cursor2.execute(sql2, (id_general,))

            for row in cursor2.fetchall():
                id_general, id_reserva = row
                reserva = {"id_reserva": id_reserva, "tipo": "Instructor"}
                reservas.append(reserva)

            # reservas de equipamientos
            cursor3 = self.connection.cursor()

            sql3 = "select * from Historial_reservas_equipamiento where id_general = %s;"
            cursor3.execute(sql3, (id_general,))

            for row in cursor3.fetchall():
                id_general, id_reserva = row
                reserva = {"id_reserva": id_reserva, "tipo": "Equipamiento"}
                reservas.append(reserva)

            return reservas

        except pymysql.Error as error:
            print("Error al obtener equipamientos:", error)

    def eliminar_reserva(self, id_reserva: int, tipo_reserva: str):
        try:
            cursor = self.connection.cursor()

            # Busca y elimina la reserva del historial correspondiente
            if tipo_reserva == "ED":
                sql_historial = "DELETE FROM Historial_reservas_ED WHERE id_reserva = %s;"
            elif tipo_reserva == "Instructor":
                sql_historial = "DELETE FROM Historial_reservas_instructor WHERE id_reserva = %s;"
            elif tipo_reserva == "Equipamiento":
                sql_historial = "DELETE FROM Historial_reservas_equipamiento WHERE id_reserva = %s;"
            cursor.execute(sql_historial, (id_reserva,))
            self.connection.commit()

            # Busca y elimina la reserva de la tabla de reservas apropiada
            if tipo_reserva == "ED":
                sql_reserva = "DELETE FROM Reservas_ED WHERE id_reserva = %s;"
            elif tipo_reserva == "Instructor":
                sql_reserva = "DELETE FROM Reservas_instructor WHERE id_reserva = %s;"
            elif tipo_reserva == "Equipamiento":
                sql_reserva = "DELETE FROM Reservas_equipamiento WHERE id_reserva = %s;"
            cursor.execute(sql_reserva, (id_reserva,))
            self.connection.commit()

            print("Reserva eliminada con éxito.")

        except pymysql.Error as error:
            print("Error al eliminar reserva:", error)

