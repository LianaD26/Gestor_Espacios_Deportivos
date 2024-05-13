from DB import DB
from Interfaz_grafica import Interfaz

db = DB(host="localhost", user="User1", password="passw2024", database="GestorED")
# si la conexión a la base de datos se da, entonces ejecuta el programa
if db.conectar():
    db.obtener_administrativos()
    db.obtener_generales()
    interfaz = Interfaz(db)
    interfaz.mostrar()
    db.desconectar()
