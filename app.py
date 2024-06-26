from DB import DB
import sqlite3
from Interfaz_grafica import Interfaz
from Almacen_info import AlmacenInfo


# si la conexión a la base de datos se da, entonces ejecuta el programa
db = DB('app.db')
if db.conectar():
    # crear los objetos de toda la información de la base de datos
    db.obtener_administrativos()
    db.obtener_generales()
    db.obtener_espacios_deportivos()
    db.obtener_instructores()
    db.obtener_equipamientos()
    interfaz = Interfaz(db)
    interfaz.mostrar()
    db.desconectar()
