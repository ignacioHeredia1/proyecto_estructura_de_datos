from src.models.mensaje import Mensaje

class Carpeta:
    def __init__(self, nombre):
        self._nombre = nombre
        self._mensajes = []
        self._subcarpetas = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def mensajes(self):
        return self._mensajes

    @property
    def subcarpetas(self):
        return self._subcarpetas

    def agregar_mensaje(self, mensaje):
        self._mensajes.append(mensaje)

    def mover_mensaje(self, mensaje, carpeta_destino):
        if mensaje in self._mensajes:
            self._mensajes.remove(mensaje)
            carpeta_destino.agregar_mensaje(mensaje)

    def agregar_subcarpeta(self, subcarpeta):
        self._subcarpetas.append(subcarpeta)

    def listar_mensajes(self):
        return self._mensajes

    def buscar_mensaje(self, criterio, valor):
        resultados = []
        for m in self._mensajes:
            if criterio == "asunto" and valor.lower() in m.asunto.lower():
                resultados.append(m)
            elif criterio == "remitente" and valor.lower() in m.remitente.lower():
                resultados.append(m)
        for sub in self._subcarpetas:
            resultados.extend(sub.buscar_mensaje(criterio, valor))
        return resultados
