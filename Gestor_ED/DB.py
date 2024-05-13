import pymysql
from Administrativo import Administrativo
from General import General
from Almacen_info import AlmacenInfo
from Espacio_deportivo import EspacioDeportivo
from Instructor import Instructor

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