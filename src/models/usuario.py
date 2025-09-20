class Usuario:
    def __init__(self, nombre, correo, contraseña):
        self._nombre = nombre
        self._correo = correo
        self._contraseña = contraseña
        self._carpetas = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, nuevo_correo):
        self._correo = nuevo_correo

    @property
    def contraseña(self):
        return self._contraseña

    @contraseña.setter
    def contraseña(self, nueva_contraseña):
        self._contraseña = nueva_contraseña

    @property
    def carpetas(self):
        return self._carpetas

    def agregar_carpeta(self, carpeta):
        self._carpetas.append(carpeta)
