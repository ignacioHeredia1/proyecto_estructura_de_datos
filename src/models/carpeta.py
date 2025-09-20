class Carpeta:
    def __init__(self, nombre):
        self._nombre = nombre
        self._mensajes = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def mensajes(self):
        return self._mensajes

    def agregar_mensaje(self, mensaje):
        self._mensajes.append(mensaje)

    def listar_mensajes(self):
        return self._mensajes
