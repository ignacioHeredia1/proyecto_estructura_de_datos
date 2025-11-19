class Carpeta:
    """
    Representa una carpeta que puede contener mensajes y subcarpetas.
    Implementa una estructura de árbol para el almacenamiento (Entrega 2).
    """
    def __init__(self, nombre):
        self._nombre = nombre
        self._mensajes = []
        self._subcarpetas = []  # Lista para recursividad (Subcarpetas)

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
        """Devuelve la lista de subcarpetas contenidas en esta carpeta."""
        return self._subcarpetas

    def agregar_mensaje(self, mensaje):
        """Agrega un mensaje a la lista local de la carpeta."""
        self._mensajes.append(mensaje)

    def eliminar_mensaje(self, mensaje):
        """
        Elimina un mensaje de la carpeta actual.
        Necesario para la funcionalidad de 'Mover mensaje' (Entrega 2).
        """
        if mensaje in self._mensajes:
            self._mensajes.remove(mensaje)

    def agregar_subcarpeta(self, carpeta):
        """
        Agrega una carpeta hija dentro de la carpeta actual (Estructura de Árbol).
        Args:
            carpeta (Carpeta): La subcarpeta a agregar.
        """
        self._subcarpetas.append(carpeta)

    def listar_mensajes(self):
        return self._mensajes

    def buscar_mensajes_recursivo(self, termino):
    
        # 1. Buscar en los mensajes de esta carpeta (Nodo actual)
        resultados = [m for m in self._mensajes if termino.lower() in m.asunto.lower()]
        
        # 2. Paso recursivo: Llamar al mismo método en cada subcarpeta (Hijos)
        for subcarpeta in self._subcarpetas:
            resultados.extend(subcarpeta.buscar_mensajes_recursivo(termino))
            
        return resultados
    