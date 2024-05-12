from DB import DB

class GestorInicioSesion:
    @classmethod
    def iniciar_sesion_administrativo(cls):
        print("Iniciar sesión como administrativo...")

    @classmethod
    def iniciar_sesion_general(cls):
        print("Iniciar sesión como general...")

    @classmethod
    def registrar_administrativo(cls):
        print("Registrarse como administrativo...")
        #DB.registrar_administrativo()

    @classmethod
    def registrar_general(cls):
        print("Registrarse como general...")

    # si inicia sesión que ese usuario exista en la base de datos
    def verificar_administrativo(self):
        pass

    def verificar_general(self):
        pass

