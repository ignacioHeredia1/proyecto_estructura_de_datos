class FiltroController:
    def filtrar_por_asunto(self, mensajes, palabra_clave):
        return [m for m in mensajes if palabra_clave.lower() in m.asunto.lower()]
