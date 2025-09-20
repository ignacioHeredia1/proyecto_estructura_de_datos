def validar_correo(correo):
    return "@" in correo and "." in correo

def generar_id():
    import uuid
    return str(uuid.uuid4())
