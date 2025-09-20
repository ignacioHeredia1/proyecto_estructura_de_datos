class Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mensajes = []

    def agregar_mensaje(self, mensaje):
        self.mensajes.append(mensaje)

    def listar_mensajes(self):
        return self.mensajes
