import heapq

class FiltroController:
    def __init__(self):
        self.reglas = {}  # diccionario: {palabra_clave: carpeta_destino}
        self._cola_prioridad = []  # heap para mensajes urgentes

    def agregar_regla(self, palabra_clave, carpeta_destino):
        """Agrega regla de filtrado: si un mensaje contiene la palabra_clave, va a carpeta_destino"""
        self.reglas[palabra_clave.lower()] = carpeta_destino

    def aplicar_filtros(self, mensaje):
        """Aplica las reglas sobre un mensaje"""
        for palabra, carpeta in self.reglas.items():
            if palabra in mensaje.asunto.lower() or palabra in mensaje.remitente.lower():
                carpeta.agregar_mensaje(mensaje)
                return True
        return False

    def marcar_urgente(self, mensaje, prioridad=1):
        """Agrega un mensaje a la cola de prioridad (menor número = más urgente)"""
        heapq.heappush(self._cola_prioridad, (prioridad, mensaje))

    def obtener_mensaje_urgente(self):
        """Saca el mensaje más urgente"""
        if self._cola_prioridad:
            return heapq.heappop(self._cola_prioridad)[1]
        return None

