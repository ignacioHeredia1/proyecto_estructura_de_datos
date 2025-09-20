class ServidorCorreo:
    def __init__(self):
        self._usuarios = {}

    def registrar_usuario(self, usuario):
        self._usuarios[usuario.correo] = usuario

    def enviar_mensaje(self, mensaje):
        destinatario = self._usuarios.get(mensaje.destinatario)
        if destinatario:
            destinatario.carpetas[0].agregar_mensaje(mensaje)
            return True
        return False

    def listar_usuarios(self):
        return list(self._usuarios.keys())
