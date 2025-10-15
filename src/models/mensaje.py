class Mensaje:
    def __init__(self, remitente, destinatario, asunto, cuerpo):
        self._remitente = remitente
        self._destinatario = destinatario
        self._asunto = asunto
        self._cuerpo = cuerpo
        self._leido = False  # ✅ nuevo atributo

    @property
    def remitente(self):
        return self._remitente

    @property
    def destinatario(self):
        return self._destinatario

    @property
    def asunto(self):
        return self._asunto

    @property
    def cuerpo(self):
        return self._cuerpo

    @property
    def leido(self):
        return self._leido

    def marcar_leido(self):
        self._leido = True

    def __str__(self):
        return f"De: {self.remitente} | Para: {self.destinatario} | Asunto: {self.asunto}"
