import tkinter as tk
from Gestor_inicio_sesion import GestorInicioSesion

class Interfaz:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de Sesión")
        self.ventana.geometry("300x200")

        # Crear el título
        self.label_titulo = tk.Label(self.ventana, text="Bienvenido")
        self.label_titulo.pack()

        # Crear los botones de Iniciar Sesión y Registrarse
        self.crear_botones_inicio()

        # Centrar la ventana en la pantalla
        self.ventana.update_idletasks()
        self.width = self.ventana.winfo_width()
        self.height = self.ventana.winfo_height()
        x = (self.ventana.winfo_screenwidth() // 2) - (self.width // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (self.height // 2)
        self.ventana.geometry('{}x{}+{}+{}'.format(self.width, self.height, x, y))

    def crear_botones_inicio(self):
        self.boton_iniciar_sesion = tk.Button(self.ventana, text="Iniciar Sesión", command=self.mostrar_opciones_iniciar_sesion, bg="blue", fg="white")
        self.boton_iniciar_sesion.pack()

        self.boton_registrarse = tk.Button(self.ventana, text="Registrarse", command=self.mostrar_opciones_registrarse, bg="green", fg="white")
        self.boton_registrarse.pack()

    def mostrar_opciones_iniciar_sesion(self):
        # Limpiar la ventana de botones anteriores
        self.limpiar_ventana()
        # Crear nuevos botones
        self.boton_regresar = tk.Button(self.ventana, text="Regresar al inicio", command=self.mostrar_inicio,
                                        relief="flat", borderwidth=5)
        self.boton_regresar.pack()
        self.boton_administrativo = tk.Button(self.ventana, text="Administrativo", command=self.iniciar_sesion_administrativo)
        self.boton_administrativo.pack()
        self.boton_general = tk.Button(self.ventana, text="General", command=self.iniciar_sesion_general)
        self.boton_general.pack()

    def mostrar_opciones_registrarse(self):
        # Limpiar la ventana de botones anteriores
        self.limpiar_ventana()
        # Crear nuevos botones
        self.boton_regresar = tk.Button(self.ventana, text="Regresar al inicio", command=self.mostrar_inicio,
                                        relief="flat", borderwidth=5)
        self.boton_regresar.pack()
        self.boton_administrativo = tk.Button(self.ventana, text="Administrativo", command=self.registrarse_administrativo)
        self.boton_administrativo.pack()
        self.boton_general = tk.Button(self.ventana, text="General", command=self.registrarse_general)
        self.boton_general.pack()

    def iniciar_sesion_administrativo(self):
        print("Iniciar sesión como administrativo...")
        #GestorInicioSesion.iniciar_sesion_administrativo()

    def iniciar_sesion_general(self):
        print("Iniciar sesión como general...")
        GestorInicioSesion.iniciar_sesion_general()

    def registrarse_administrativo(self):
        print("Registrarse como administrativo...")
        GestorInicioSesion.registrar_administrativo()

    def registrarse_general(self):
        print("Registrarse como general...")
        GestorInicioSesion.registrar_general()

    def mostrar_inicio(self):
        # limpiar la ventana de todos los widgets
        self.limpiar_ventana()

        self.label_titulo = tk.Label(self.ventana, text="Bienvenido")
        self.label_titulo.pack()

        # crear los botones del inicio
        self.crear_botones_inicio()

    def limpiar_ventana(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def mostrar(self):
        self.ventana.mainloop()

