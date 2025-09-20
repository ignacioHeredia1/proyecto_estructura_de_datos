from src.models.usuario import Usuario

u = Usuario("Test", "test@mail.com", "clave")
print(f"Import OK: {u.nombre}")