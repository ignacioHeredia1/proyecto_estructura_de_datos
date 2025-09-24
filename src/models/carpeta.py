# src/models/carpeta.py
class Carpeta:
    def __init__(self, nombre):
        self._nombre = nombre
        self._mensajes = []
        self._subcarpetas = []  # lista de subcarpetas (recursivo)

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
        """Mueve un mensaje de esta carpeta a otra"""
        if mensaje in self._mensajes:
            self._mensajes.remove(mensaje)
            carpeta_destino.agregar_mensaje(mensaje)

    def agregar_subcarpeta(self, subcarpeta):
        """Agrega una subcarpeta"""
        self._subcarpetas.append(subcarpeta)

    def listar_mensajes(self):
        return self._mensajes

    def buscar_mensaje(self, criterio, valor):
        """
        Búsqueda recursiva en esta carpeta y subcarpetas.
        criterio: 'asunto' o 'remitente'
        valor: texto a buscar
        """
        resultados = []

        # Buscar en los mensajes de esta carpeta
        for m in self._mensajes:
            if criterio == "asunto" and valor.lower() in m.asunto.lower():
                resultados.append(m)
            elif criterio == "remitente" and valor.lower() in m.remitente.lower():
                resultados.append(m)

        # Buscar recursivamente en subcarpetas
        for sub in self._subcarpetas:
            resultados.extend(sub.buscar_mensaje(criterio, valor))

        return resultados
