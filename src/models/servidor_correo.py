class ServidorCorreo:
    def __init__(self):
        self._usuarios = {}  
    def registrar_usuario(self, usuario):
        self._usuarios[usuario.correo] = usuario

    def listar_usuarios(self):
        return list(self._usuarios.keys())

    def obtener_usuario(self, correo):
        return self._usuarios.get(correo)
