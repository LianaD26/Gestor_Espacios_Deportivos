import tkinter as tk
from Gestor_inicio_sesion import GestorInicioSesion
from Gestor_espacio_deportivo import GestorED
from Gestor_reserva import GestorReserva


class Interfaz:
    def __init__(self, db):
        self.db = db
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de Sesión")
        self.ventana.geometry("300x200")

        self.label_titulo = tk.Label(self.ventana, text="Bienvenido")
        self.label_titulo.pack()

        # botones de Iniciar Sesión y Registrarse
        self.crear_botones_inicio()

        # ventana general en la pantalla
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

        def iniciar_admin():
            documento = entrada_documento.get()
            ctr = entrada_contr.get()

            if documento and ctr:
                ventana_inicio.destroy()
                if GestorInicioSesion.iniciar_sesion_administrativo(int(documento), ctr):
                    self.limpiar_ventana()
                    boton_agregar_espacio = tk.Button(self.ventana, text="Agregar espacio deportivo",
                                                      command=self.agregar_espacio_deportivo)
                    boton_agregar_espacio.pack()
                    boton_eliminar_espacio = tk.Button(self.ventana, text="Eliminar espacio deportivo",
                                                       command=self.eliminar_espacio_deportivo)
                    boton_eliminar_espacio.pack()
                else:
                    mensaje_no_coincide = tk.Label(self.ventana, text="Datos no coinciden.", fg="red")
                    mensaje_no_coincide.pack()

            else:
                # Mostrar un mensaje de error si los campos están vacíos
                mensaje_error = tk.Label(ventana_inicio, text="Por favor, complete todos los campos.", fg="red")
                mensaje_error.pack()

        # Crear el botón de registro
        boton_iniciar_sesion = tk.Button(ventana_inicio, text="Iniciar sesión", command=iniciar_admin)
        boton_iniciar_sesion.pack()

        ventana_inicio.geometry("400x250")

        # Centrar la ventana en la pantalla
        ventana_inicio.update_idletasks()
        x = (ventana_inicio.winfo_screenwidth() // 2) - (ventana_inicio.winfo_width() // 2)
        y = (ventana_inicio.winfo_screenheight() // 2) - (ventana_inicio.winfo_height() // 2)
        ventana_inicio.geometry('+{}+{}'.format(x, y))

    def agregar_espacio_deportivo(self):
        # id espacio, nombre, reglamento, capacidad
        ventana_ED = tk.Toplevel(self.ventana)
        ventana_ED.title("Agregar espacio deportivo")

        # Crear los campos de entrada
        label_id = tk.Label(ventana_ED, text="Id espacio:")
        label_id.pack()
        entrada_id = tk.Entry(ventana_ED)
        entrada_id.pack()

        label_espacio = tk.Label(ventana_ED, text="Nombre espacio:")
        label_espacio.pack()
        entrada_nombre = tk.Entry(ventana_ED)
        entrada_nombre.pack()

        label_reglamento = tk.Label(ventana_ED, text="Reglamento:")
        label_reglamento.pack()
        entrada_reglamento = tk.Entry(ventana_ED)
        entrada_reglamento.pack()

        label_capacidad = tk.Label(ventana_ED, text="Capacidad:")
        label_capacidad.pack()
        entrada_capacidad = tk.Entry(ventana_ED)
        entrada_capacidad.pack()

        def registrar_espacio():
            id_espacio = entrada_id.get()
            nombre = entrada_nombre.get()
            reglamento = entrada_reglamento.get()
            capacidad = entrada_capacidad.get()

            if id_espacio and nombre and reglamento and capacidad:
                GestorED.agregar_espacio_deportivo(int(id_espacio), nombre, reglamento, int(capacidad), self.db)
                ventana_ED.destroy()
            else:
                # Mostrar un mensaje de error si los campos están vacíos
                mensaje_error = tk.Label(ventana_ED, text="Por favor, complete todos los campos.", fg="red")
                mensaje_error.pack()

        # Crear el botón de agregar
        boton_registrar = tk.Button(ventana_ED, text="Agregar", command=registrar_espacio)
        boton_registrar.pack()

        ventana_ED.geometry("400x250")

        # Centrar la ventana en la pantalla
        ventana_ED.update_idletasks()
        x = (ventana_ED.winfo_screenwidth() // 2) - (ventana_ED.winfo_width() // 2)
        y = (ventana_ED.winfo_screenheight() // 2) - (ventana_ED.winfo_height() // 2)
        ventana_ED.geometry('+{}+{}'.format(x, y))

    def eliminar_espacio_deportivo(self):
        ventana_ED = tk.Toplevel(self.ventana)
        ventana_ED.title("Eliminar espacio deportivo")

        # Crear los campos de entrada
        label_id = tk.Label(ventana_ED, text="Id espacio:")
        label_id.pack()
        entrada_id = tk.Entry(ventana_ED)
        entrada_id.pack()

        def eliminar_espacio():
            id_espacio = entrada_id.get()

            if id_espacio:
                GestorED.eliminar_espacio_deportivo(int(id_espacio), self.db)
                ventana_ED.destroy()
            else:
                # Mostrar un mensaje de error si los campos están vacíos
                mensaje_error = tk.Label(ventana_ED, text="Por favor, complete todos los campos.", fg="red")
                mensaje_error.pack()

        # Crear el botón de eliminar
        boton_eliminar = tk.Button(ventana_ED, text="Eliminar", command=eliminar_espacio)
        boton_eliminar.pack()

        ventana_ED.geometry("400x250")

        # Centrar la ventana en la pantalla
        ventana_ED.update_idletasks()
        x = (ventana_ED.winfo_screenwidth() // 2) - (ventana_ED.winfo_width() // 2)
        y = (ventana_ED.winfo_screenheight() // 2) - (ventana_ED.winfo_height() // 2)
        ventana_ED.geometry('+{}+{}'.format(x, y))

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
                ventana_inicio.destroy()
                if GestorInicioSesion.iniciar_sesion_general(int(documento), ctr):
                    self.limpiar_ventana()
                    boton_reserva_ED = tk.Button(self.ventana, text="Reserva espacios deportivos",
                                                      command= lambda: self.gestionar_reservas_ED(int(documento)))
                    boton_reserva_ED.pack()
                    boton_reserva_instructor = tk.Button(self.ventana, text="Reserva instructor",
                                                      command= lambda: self.gestionar_reservas_instructor(int(documento)))
                    boton_reserva_instructor.pack()
                    boton_reserva_equipamiento = tk.Button(self.ventana, text="Reserva equipamiento",
                                                      command= lambda: self.gestionar_reservas_equipamiento(int(documento)))
                    boton_reserva_equipamiento.pack()

                    boton_mostrar_reservas = tk.Button(self.ventana, text="Mostrar mis reservas",
                                                       command=lambda: self.mostrar_mis_reservas(int(documento)))
                    boton_mostrar_reservas.pack()
                    boton_eliminar_reserva = tk.Button(self.ventana, text="Eliminar reserva",
                                                       command=lambda: self.eliminar_reserva(int(documento)))
                    boton_eliminar_reserva.pack()

                else:
                    mensaje_no_coincide = tk.Label(self.ventana, text="Datos no coinciden.", fg="red")
                    mensaje_no_coincide.pack()

            else:
                # Mostrar un mensaje de error si los campos están vacíos
                mensaje_error = tk.Label(ventana_inicio, text="Por favor, complete todos los campos.", fg="red")
                mensaje_error.pack()

        # Crear el botón de registro
        boton_iniciar_sesion = tk.Button(ventana_inicio, text="Iniciar sesión", command=iniciar_general)
        boton_iniciar_sesion.pack()

        ventana_inicio.geometry("400x250")

        # Centrar la ventana en la pantalla
        ventana_inicio.update_idletasks()
        x = (ventana_inicio.winfo_screenwidth() // 2) - (ventana_inicio.winfo_width() // 2)
        y = (ventana_inicio.winfo_screenheight() // 2) - (ventana_inicio.winfo_height() // 2)
        ventana_inicio.geometry('+{}+{}'.format(x, y))

    def gestionar_reservas_ED(self, id_general: int):
        ventana_reserva_ED = tk.Toplevel(self.ventana)
        ventana_reserva_ED.title("Gestionar reservas ED")

        boton_mostrar_ED = tk.Button(ventana_reserva_ED, text="Mostrar espacios deportivos",
                                          command=self.mostrar_espacios_deportivos)
        boton_mostrar_ED.pack()
        boton_agendar_ED= tk.Button(ventana_reserva_ED, text="Agendar espacio deportivo",
                                           command=lambda: self.agendar_espacio_deportivo(id_general))
        boton_agendar_ED.pack()

        ventana_reserva_ED.geometry("400x250")

        # Centrar la ventana en la pantalla
        ventana_reserva_ED.update_idletasks()
        x = (ventana_reserva_ED.winfo_screenwidth() // 2) - (ventana_reserva_ED.winfo_width() // 2)
        y = (ventana_reserva_ED.winfo_screenheight() // 2) - (ventana_reserva_ED.winfo_height() // 2)
        ventana_reserva_ED.geometry('+{}+{}'.format(x, y))

    def mostrar_mis_reservas(self, id_general: int):
        ventana_mostrar = tk.Toplevel()
        ventana_mostrar.title("Mis reservas")

        # Crear un Frame para contener el widget Text y el Scrollbar
        frame = tk.Frame(ventana_mostrar)
        frame.pack(fill=tk.BOTH, expand=True)

        # Crear el widget Text
        text_area = tk.Text(frame, wrap=tk.WORD)
        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Crear el Scrollbar y asociarlo al widget Text
        scrollbar = tk.Scrollbar(frame, command=text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.configure(yscrollcommand=scrollbar.set)

        reservas = self.db.mostrar_reservas_general(int(id_general))
        for e in reservas:
            cadena_formateada = ""
            for clave, valor in e.items():
                cadena_formateada += f"{clave}: {valor}\n"
            text_area.insert(tk.END, cadena_formateada + "---------------------------------------\n")

        ventana_mostrar.update_idletasks()
        x = (ventana_mostrar.winfo_screenwidth() // 2) - (ventana_mostrar.winfo_width() // 2)
        y = (ventana_mostrar.winfo_screenheight() // 2) - (ventana_mostrar.winfo_height() // 2)
        ventana_mostrar.geometry('+{}+{}'.format(x, y))
        ventana_mostrar.geometry("700x400")  # Aumentar la altura de la ventana
        ventana_mostrar.mainloop()

    def eliminar_reserva(self, id_general: int):
        ventana_ED = tk.Toplevel(self.ventana)
        ventana_ED.title("Eliminar reserva")

        # Crear los campos de entrada
        label_id = tk.Label(ventana_ED, text="Id reserva:")
        label_id.pack()
        entrada_id = tk.Entry(ventana_ED)
        entrada_id.pack()

        label_tipo = tk.Label(ventana_ED, text="Tipo de reserva(ED, Instructor o Equipamiento):")
        label_tipo.pack()
        entrada_tipo = tk.Entry(ventana_ED)
        entrada_tipo.pack()

        def eliminar_reserva():
            id_reserva = entrada_id.get()
            tipo_reserva = entrada_tipo.get()

            if id_reserva and tipo_reserva:
                self.db.eliminar_reserva(int(id_reserva), tipo_reserva)
                ventana_ED.destroy()
            else:
                # Mostrar un mensaje de error si los campos están vacíos
                mensaje_error = tk.Label(ventana_ED, text="Por favor, complete todos los campos.", fg="red")
                mensaje_error.pack()

        # Crear el botón de eliminar
        boton_eliminar = tk.Button(ventana_ED, text="Eliminar", command=eliminar_reserva)
        boton_eliminar.pack()

        ventana_ED.geometry("400x250")

        # Centrar la ventana en la pantalla
        ventana_ED.update_idletasks()
        x = (ventana_ED.winfo_screenwidth() // 2) - (ventana_ED.winfo_width() // 2)
        y = (ventana_ED.winfo_screenheight() // 2) - (ventana_ED.winfo_height() // 2)
        ventana_ED.geometry('+{}+{}'.format(x, y))

    def mostrar_espacios_deportivos(self):
        ventana_mostrar = tk.Toplevel()
        ventana_mostrar.title("Espacios deportivos")

        # Crear un Frame para contener el widget Text y el Scrollbar
        frame = tk.Frame(ventana_mostrar)
        frame.pack(fill=tk.BOTH, expand=True)

        # Crear el widget Text
        text_area = tk.Text(frame, wrap=tk.WORD)
        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Crear el Scrollbar y asociarlo al widget Text
        scrollbar = tk.Scrollbar(frame, command=text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.configure(yscrollcommand=scrollbar.set)

        espacios = GestorReserva.mostrar_espacios_deportivo()
        for e in espacios:
            cadena_formateada = ""
            for clave, valor in e.items():
                cadena_formateada += f"{clave}: {valor}\n"
            text_area.insert(tk.END, cadena_formateada + "---------------------------------------\n")

        ventana_mostrar.update_idletasks()
        x = (ventana_mostrar.winfo_screenwidth() // 2) - (ventana_mostrar.winfo_width() // 2)
        y = (ventana_mostrar.winfo_screenheight() // 2) - (ventana_mostrar.winfo_height() // 2)
        ventana_mostrar.geometry('+{}+{}'.format(x, y))
        ventana_mostrar.geometry("700x400")  # Aumentar la altura de la ventana
        ventana_mostrar.mainloop()

    def agendar_espacio_deportivo(self, id_general: int):
        ventana_agendar = tk.Toplevel(self.ventana)
        ventana_agendar.title("Agendar ED")

        # Crear los campos de entrada
        label_id = tk.Label(ventana_agendar, text="Id espacio a reservar:")
        label_id.pack()
        entrada_id = tk.Entry(ventana_agendar)
        entrada_id.pack()

        label_hora_inicio = tk.Label(ventana_agendar, text="Hora inicio(ej: 1200):")
        label_hora_inicio.pack()
        entrada_hora_inicio = tk.Entry(ventana_agendar)
        entrada_hora_inicio.pack()

        label_hora_fin = tk.Label(ventana_agendar, text="Hora fin(ej: 1400):")
        label_hora_fin.pack()
        entrada_hora_fin = tk.Entry(ventana_agendar)
        entrada_hora_fin.pack()

        def agendar():
            id = entrada_id.get()
            inicio = entrada_hora_inicio.get()
            fin = entrada_hora_fin.get()

            if id and inicio and fin:
                ventana_agendar.destroy()
                if GestorReserva.agendar_espacio_deportivo(id_general, int(id), int(inicio), int(fin), self.db):
                    mensaje_agendado = tk.Label(self.ventana, text="Espacio deportivo agendado con éxito!.", fg="blue")
                    mensaje_agendado.pack()
                else:
                    mensaje_no_coincide = tk.Label(self.ventana, text="Datos no coinciden.", fg="red")
                    mensaje_no_coincide.pack()

            else:
                # Mostrar un mensaje de error si los campos están vacíos
                mensaje_error = tk.Label(ventana_agendar, text="Por favor, complete todos los campos.", fg="red")
                mensaje_error.pack()

        # Crear el botón de registro
        boton_agendar = tk.Button(ventana_agendar, text="Agendar", command=agendar)
        boton_agendar.pack()

        ventana_agendar.geometry("400x250")

        # Centrar la ventana en la pantalla
        ventana_agendar.update_idletasks()
        x = (ventana_agendar.winfo_screenwidth() // 2) - (ventana_agendar.winfo_width() // 2)
        y = (ventana_agendar.winfo_screenheight() // 2) - (ventana_agendar.winfo_height() // 2)
        ventana_agendar.geometry('+{}+{}'.format(x, y))

    def gestionar_reservas_instructor(self, id_general: int):
        ventana_reserva_instructor = tk.Toplevel(self.ventana)
        ventana_reserva_instructor.title("Gestionar reservas ED")

        boton_mostrar_instructor = tk.Button(ventana_reserva_instructor, text="Mostrar instructores",
                                     command=self.mostrar_instructores)
        boton_mostrar_instructor.pack()
        boton_agendar_instructor = tk.Button(ventana_reserva_instructor, text="Agendar instructor",
                                     command= lambda: self.agendar_instructor(id_general))
        boton_agendar_instructor.pack()

        ventana_reserva_instructor.geometry("400x250")

        # Centrar la ventana en la pantalla
        ventana_reserva_instructor.update_idletasks()
        x = (ventana_reserva_instructor.winfo_screenwidth() // 2) - (ventana_reserva_instructor.winfo_width() // 2)
        y = (ventana_reserva_instructor.winfo_screenheight() // 2) - (ventana_reserva_instructor.winfo_height() // 2)
        ventana_reserva_instructor.geometry('+{}+{}'.format(x, y))

    def mostrar_instructores(self):
        ventana_mostrar = tk.Toplevel()
        ventana_mostrar.title("Instructores")

        # Crear un Frame para contener el widget Text y el Scrollbar
        frame = tk.Frame(ventana_mostrar)
        frame.pack(fill=tk.BOTH, expand=True)

        # Crear el widget Text
        text_area = tk.Text(frame, wrap=tk.WORD)
        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Crear el Scrollbar y asociarlo al widget Text
        scrollbar = tk.Scrollbar(frame, command=text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.configure(yscrollcommand=scrollbar.set)

        espacios = GestorReserva.mostrar_instructores()
        for e in espacios:
            cadena_formateada = ""
            for clave, valor in e.items():
                cadena_formateada += f"{clave}: {valor}\n"
            text_area.insert(tk.END, cadena_formateada + "---------------------------------------\n")

        ventana_mostrar.update_idletasks()
        x = (ventana_mostrar.winfo_screenwidth() // 2) - (ventana_mostrar.winfo_width() // 2)
        y = (ventana_mostrar.winfo_screenheight() // 2) - (ventana_mostrar.winfo_height() // 2)
        ventana_mostrar.geometry('+{}+{}'.format(x, y))
        ventana_mostrar.geometry("700x400")  # Aumentar la altura de la ventana
        ventana_mostrar.mainloop()

    def agendar_instructor(self, id_general: int):
        ventana_agendar = tk.Toplevel(self.ventana)
        ventana_agendar.title("Agendar instructor")

        # Crear los campos de entrada
        label_id = tk.Label(ventana_agendar, text="Id instructor a reservar:")
        label_id.pack()
        entrada_id = tk.Entry(ventana_agendar)
        entrada_id.pack()

        label_hora_inicio = tk.Label(ventana_agendar, text="Hora inicio(ej: 1200):")
        label_hora_inicio.pack()
        entrada_hora_inicio = tk.Entry(ventana_agendar)
        entrada_hora_inicio.pack()

        label_hora_fin = tk.Label(ventana_agendar, text="Hora fin(ej: 1400):")
        label_hora_fin.pack()
        entrada_hora_fin = tk.Entry(ventana_agendar)
        entrada_hora_fin.pack()

        def agendar():
            id = entrada_id.get()
            inicio = entrada_hora_inicio.get()
            fin = entrada_hora_fin.get()

            if id and inicio and fin:
                ventana_agendar.destroy()
                if GestorReserva.agendar_instructor(id_general, int(id), int(inicio), int(fin), self.db):
                    mensaje_agendado = tk.Label(self.ventana, text="Instructor agendado con éxito!.", fg="blue")
                    mensaje_agendado.pack()
                else:
                    mensaje_no_coincide = tk.Label(self.ventana, text="Datos no coinciden.", fg="red")
                    mensaje_no_coincide.pack()

            else:
                # Mostrar un mensaje de error si los campos están vacíos
                mensaje_error = tk.Label(ventana_agendar, text="Por favor, complete todos los campos.", fg="red")
                mensaje_error.pack()

        # Crear el botón de registro
        boton_agendar = tk.Button(ventana_agendar, text="Agendar", command=agendar)
        boton_agendar.pack()

        ventana_agendar.geometry("400x250")

        # Centrar la ventana en la pantalla
        ventana_agendar.update_idletasks()
        x = (ventana_agendar.winfo_screenwidth() // 2) - (ventana_agendar.winfo_width() // 2)
        y = (ventana_agendar.winfo_screenheight() // 2) - (ventana_agendar.winfo_height() // 2)
        ventana_agendar.geometry('+{}+{}'.format(x, y))

    def gestionar_reservas_equipamiento(self, id_general: int):
        ventana_reserva_equipo = tk.Toplevel(self.ventana)
        ventana_reserva_equipo.title("Gestionar reservas ED")

        boton_mostrar_equipo = tk.Button(ventana_reserva_equipo, text="Mostrar equipamientos",
                                     command=self.mostrar_equipamiento)
        boton_mostrar_equipo.pack()
        boton_agendar_equipo = tk.Button(ventana_reserva_equipo, text="Agendar equipamiento",
                                     command= lambda: self.agendar_equipamiento(id_general))
        boton_agendar_equipo.pack()

        ventana_reserva_equipo.geometry("400x250")

        # Centrar la ventana en la pantalla
        ventana_reserva_equipo.update_idletasks()
        x = (ventana_reserva_equipo.winfo_screenwidth() // 2) - (ventana_reserva_equipo.winfo_width() // 2)
        y = (ventana_reserva_equipo.winfo_screenheight() // 2) - (ventana_reserva_equipo.winfo_height() // 2)
        ventana_reserva_equipo.geometry('+{}+{}'.format(x, y))

    def mostrar_equipamiento(self):
        ventana_mostrar = tk.Toplevel()
        ventana_mostrar.title("Equipamientos")

        # Crear un Frame para contener el widget Text y el Scrollbar
        frame = tk.Frame(ventana_mostrar)
        frame.pack(fill=tk.BOTH, expand=True)

        # Crear el widget Text
        text_area = tk.Text(frame, wrap=tk.WORD)
        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Crear el Scrollbar y asociarlo al widget Text
        scrollbar = tk.Scrollbar(frame, command=text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.configure(yscrollcommand=scrollbar.set)

        equipamiento = GestorReserva.mostrar_equipamiento()
        for e in equipamiento:
            cadena_formateada = ""
            for clave, valor in e.items():
                cadena_formateada += f"{clave}: {valor}\n"
            text_area.insert(tk.END, cadena_formateada + "---------------------------------------\n")

        ventana_mostrar.update_idletasks()
        x = (ventana_mostrar.winfo_screenwidth() // 2) - (ventana_mostrar.winfo_width() // 2)
        y = (ventana_mostrar.winfo_screenheight() // 2) - (ventana_mostrar.winfo_height() // 2)
        ventana_mostrar.geometry('+{}+{}'.format(x, y))
        ventana_mostrar.geometry("700x400")  # Aumentar la altura de la ventana
        ventana_mostrar.mainloop()

    def agendar_equipamiento(self, id_general: int):
        ventana_agendar = tk.Toplevel(self.ventana)
        ventana_agendar.title("Agendar Equipamiento")

        # Crear los campos de entrada
        label_id = tk.Label(ventana_agendar, text="Id equipamiento a reservar:")
        label_id.pack()
        entrada_id = tk.Entry(ventana_agendar)
        entrada_id.pack()

        label_hora_inicio = tk.Label(ventana_agendar, text="Hora inicio(ej: 1200):")
        label_hora_inicio.pack()
        entrada_hora_inicio = tk.Entry(ventana_agendar)
        entrada_hora_inicio.pack()

        label_hora_fin = tk.Label(ventana_agendar, text="Hora fin(ej: 1400):")
        label_hora_fin.pack()
        entrada_hora_fin = tk.Entry(ventana_agendar)
        entrada_hora_fin.pack()

        def agendar():
            id = entrada_id.get()
            inicio = entrada_hora_inicio.get()
            fin = entrada_hora_fin.get()

            if id and inicio and fin:
                ventana_agendar.destroy()
                if GestorReserva.agendar_equipamiento(id_general, int(id), int(inicio), int(fin), self.db):
                    mensaje_agendado = tk.Label(self.ventana, text="Equipamiento agendado con éxito!.", fg="blue")
                    mensaje_agendado.pack()
                else:
                    mensaje_no_coincide = tk.Label(self.ventana, text="Datos no coinciden.", fg="red")
                    mensaje_no_coincide.pack()

            else:
                # Mostrar un mensaje de error si los campos están vacíos
                mensaje_error = tk.Label(ventana_agendar, text="Por favor, complete todos los campos.", fg="red")
                mensaje_error.pack()

        # Crear el botón de registro
        boton_agendar = tk.Button(ventana_agendar, text="Agendar", command=agendar)
        boton_agendar.pack()

        ventana_agendar.geometry("400x250")

        # Centrar la ventana en la pantalla
        ventana_agendar.update_idletasks()
        x = (ventana_agendar.winfo_screenwidth() // 2) - (ventana_agendar.winfo_width() // 2)
        y = (ventana_agendar.winfo_screenheight() // 2) - (ventana_agendar.winfo_height() // 2)
        ventana_agendar.geometry('+{}+{}'.format(x, y))

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

        ventana_registro.geometry("400x250")

        # Centrar la ventana en la pantalla
        ventana_registro.update_idletasks()
        x = (ventana_registro.winfo_screenwidth() // 2) - (ventana_registro.winfo_width() // 2)
        y = (ventana_registro.winfo_screenheight() // 2) - (ventana_registro.winfo_height() // 2)
        ventana_registro.geometry('+{}+{}'.format(x, y))

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

        ventana_registro.geometry("400x250")

        # Centrar la ventana en la pantalla
        ventana_registro.update_idletasks()
        x = (ventana_registro.winfo_screenwidth() // 2) - (ventana_registro.winfo_width() // 2)
        y = (ventana_registro.winfo_screenheight() // 2) - (ventana_registro.winfo_height() // 2)
        ventana_registro.geometry('+{}+{}'.format(x, y))

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

