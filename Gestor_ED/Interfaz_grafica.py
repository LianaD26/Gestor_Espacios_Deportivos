import tkinter as tk
from Gestor_inicio_sesion import GestorInicioSesion

class Interfaz:
    def __init__(self, db):
        self.db = db
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
        ventana_inicio = tk.Toplevel(self.ventana)
        ventana_inicio.title("Iniciar sesión Administrativo")

        # Crear los campos de entrada
        label_documento = tk.Label(ventana_inicio, text="Documento de Identidad:")
        label_documento.pack()
        entrada_documento = tk.Entry(ventana_inicio)
        entrada_documento.pack()

        label_contr = tk.Label(ventana_inicio, text="Contraseña:")
        label_contr.pack()
        entrada_contr = tk.Entry(ventana_inicio)
        entrada_contr.pack()

        def iniciar_general():
            documento = entrada_documento.get()
            ctr = entrada_contr.get()

            if documento and ctr:
                GestorInicioSesion.iniciar_sesion_administrativo(int(documento), ctr)
                ventana_inicio.destroy()
                self.limpiar_ventana()
                boton_agregar_espacio = tk.Button(self.ventana, text="Agregar espacio deportivo",
                                                      command=self.agregar_espacio_deportivo)
                boton_agregar_espacio.pack()
                boton_eliminar_espacio = tk.Button(self.ventana, text="Eliminar espacio deportivo",
                                                  command=self.eliminar_espacio_deportivo)
                boton_eliminar_espacio.pack()
            else:
                # Mostrar un mensaje de error si los campos están vacíos
                mensaje_error = tk.Label(ventana_inicio, text="Por favor, complete todos los campos.", fg="red")
                mensaje_error.pack()

        # Crear el botón de registro
        boton_iniciar_sesion = tk.Button(ventana_inicio, text="Iniciar sesión", command=iniciar_general)
        boton_iniciar_sesion.pack()

    def agregar_espacio_deportivo(self):
        pass

    def eliminar_espacio_deportivo(self):
        pass

    def iniciar_sesion_general(self):
        ventana_inicio = tk.Toplevel(self.ventana)
        ventana_inicio.title("Iniciar sesión General")

        # Crear los campos de entrada
        label_documento = tk.Label(ventana_inicio, text="Documento de Identidad:")
        label_documento.pack()
        entrada_documento = tk.Entry(ventana_inicio)
        entrada_documento.pack()

        label_contr = tk.Label(ventana_inicio, text="Contraseña:")
        label_contr.pack()
        entrada_contr = tk.Entry(ventana_inicio)
        entrada_contr.pack()

        def iniciar_general():
            documento = entrada_documento.get()
            ctr = entrada_contr.get()

            if documento and ctr:
                GestorInicioSesion.iniciar_sesion_general(int(documento), ctr)
                ventana_inicio.destroy()
                self.limpiar_ventana()
                boton_agregar_reserva = tk.Button(self.ventana, text="Agregar espacio deportivo",
                                                  command=self.agregar_reserva)
                boton_agregar_reserva.pack()
                boton_mostrar_reservas = tk.Button(self.ventana, text="Agregar espacio deportivo",
                                                  command=self.mostrar_reservas)
                boton_mostrar_reservas.pack()
                boton_eliminar_reserva = tk.Button(self.ventana, text="Agregar espacio deportivo",
                                                  command=self.eliminar_reserva)
                boton_eliminar_reserva.pack()

            else:
                # Mostrar un mensaje de error si los campos están vacíos
                mensaje_error = tk.Label(ventana_inicio, text="Por favor, complete todos los campos.", fg="red")
                mensaje_error.pack()

        # Crear el botón de registro
        boton_iniciar_sesion = tk.Button(ventana_inicio, text="Iniciar sesión", command=iniciar_general)
        boton_iniciar_sesion.pack()

    def agregar_reserva(self):
        pass

    def eliminar_reserva(self):
        pass

    def mostrar_reservas(self):
        pass

    def registrarse_administrativo(self):
        ventana_registro = tk.Toplevel(self.ventana)
        ventana_registro.title("Registro de Administrador")

        # Crear los campos de entrada
        label_documento = tk.Label(ventana_registro, text="Documento de Identidad:")
        label_documento.pack()
        entrada_documento = tk.Entry(ventana_registro)
        entrada_documento.pack()

        label_nombre = tk.Label(ventana_registro, text="Nombre:")
        label_nombre.pack()
        entrada_nombre = tk.Entry(ventana_registro)
        entrada_nombre.pack()

        label_apellido = tk.Label(ventana_registro, text="Apellido:")
        label_apellido.pack()
        entrada_apellido = tk.Entry(ventana_registro)
        entrada_apellido.pack()

        label_correo= tk.Label(ventana_registro, text="Correo:")
        label_correo.pack()
        entrada_correo = tk.Entry(ventana_registro)
        entrada_correo.pack()

        label_contr = tk.Label(ventana_registro, text="Contraseña:")
        label_contr.pack()
        entrada_contr = tk.Entry(ventana_registro)
        entrada_contr.pack()

        # Validar y registrar al Administrador
        def registrar_administrador():
            nombre = entrada_nombre.get()
            documento = entrada_documento.get()
            apellido = entrada_apellido.get()
            correo = entrada_correo.get()
            ctr = entrada_contr.get()

            if nombre and documento and apellido and correo and ctr:
                GestorInicioSesion.registrar_administrativo(int(documento), nombre, apellido, correo, ctr, self.db)
                ventana_registro.destroy()
            else:
                # Mostrar un mensaje de error si los campos están vacíos
                mensaje_error = tk.Label(ventana_registro, text="Por favor, complete todos los campos.", fg="red")
                mensaje_error.pack()

        # Crear el botón de registro
        boton_registrar = tk.Button(ventana_registro, text="Registrar", command=registrar_administrador)
        boton_registrar.pack()

    def registrarse_general(self):
        print("Registrarse como general...")
        ventana_registro = tk.Toplevel(self.ventana)
        ventana_registro.title("Registro de General")

        # Crear los campos de entrada
        label_documento = tk.Label(ventana_registro, text="Documento de Identidad:")
        label_documento.pack()
        entrada_documento = tk.Entry(ventana_registro)
        entrada_documento.pack()

        label_nombre = tk.Label(ventana_registro, text="Nombre:")
        label_nombre.pack()
        entrada_nombre = tk.Entry(ventana_registro)
        entrada_nombre.pack()

        label_apellido = tk.Label(ventana_registro, text="Apellido:")
        label_apellido.pack()
        entrada_apellido = tk.Entry(ventana_registro)
        entrada_apellido.pack()

        label_correo = tk.Label(ventana_registro, text="Correo:")
        label_correo.pack()
        entrada_correo = tk.Entry(ventana_registro)
        entrada_correo.pack()

        label_contr = tk.Label(ventana_registro, text="Contraseña:")
        label_contr.pack()
        entrada_contr = tk.Entry(ventana_registro)
        entrada_contr.pack()

        # Validar y registrar al General
        def registrar_administrador():
            nombre = entrada_nombre.get()
            documento = entrada_documento.get()
            apellido = entrada_apellido.get()
            correo = entrada_correo.get()
            ctr = entrada_contr.get()

            if nombre and documento and apellido and correo and ctr:
                GestorInicioSesion.registrar_general(int(documento), nombre, apellido, correo, ctr, self.db)
                ventana_registro.destroy()
            else:
                # Mostrar un mensaje de error si los campos están vacíos
                mensaje_error = tk.Label(ventana_registro, text="Por favor, complete todos los campos.", fg="red")
                mensaje_error.pack()

        # Crear el botón de registro
        boton_registrar = tk.Button(ventana_registro, text="Registrar", command=registrar_administrador)
        boton_registrar.pack()

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

