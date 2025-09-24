import unittest
from src.models.usuario import Usuario

class TestUsuario(unittest.TestCase):
    def test_creacion_usuario(self):
        u = Usuario("Juan", "juan@mail.com", "1234")
        self.assertEqual(u.nombre, "Juan")
