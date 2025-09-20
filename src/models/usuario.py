class Usuario:
    def __init__(self, nombre, correo, contraseña):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.carpetas = []

    def agregar_carpeta(self, carpeta):
        self.carpetas.append(carpeta)

