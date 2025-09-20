from src.models.mensaje import Mensaje

class EmailController:
    def enviar_mensaje(self, remitente, destinatario, asunto, cuerpo):
        mensaje = Mensaje(remitente, destinatario, asunto, cuerpo)
        destinatario.carpetas[0].agregar_mensaje(mensaje)
