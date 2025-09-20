class Mensaje:
    def __init__(self, remitente, destinatario, asunto, cuerpo):
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.cuerpo = cuerpo
        self.leido = False

    def marcar_leido(self):
        self.leido = True
