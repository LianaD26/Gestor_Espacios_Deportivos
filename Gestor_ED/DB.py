import pymysql
from Administrativo import Administrativo
from General import General

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

# falta añadir las funciones para hacer el CRUD en las tablas y falta crear esas tablas,
# lo cual peudo realizarlo desde la consola de mariadb
