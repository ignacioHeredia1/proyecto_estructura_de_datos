import unittest
from src.models.carpeta import Carpeta
from src.models.mensaje import Mensaje

class TestEntrega2(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        # Estructura de Árbol: Raiz -> Trabajo -> Importante
        self.raiz = Carpeta("Bandeja de Entrada")
        self.sub_trabajo = Carpeta("Trabajo")
        self.sub_importante = Carpeta("Importante")
        
        # Construcción del árbol (Entrega 2)
        self.raiz.agregar_subcarpeta(self.sub_trabajo)
        self.sub_trabajo.agregar_subcarpeta(self.sub_importante)

    def test_busqueda_profunda(self):
        """Verifica que encuentre un mensaje usando recursividad en niveles profundos"""
        msg = Mensaje("jefe@mail.com", "yo@mail.com", "Reunion Urgente", "...")
        self.sub_importante.agregar_mensaje(msg)
        
        # Busca desde la raíz, el mensaje está 2 niveles más abajo
        resultados = self.raiz.buscar_mensajes_recursivo("Urgente")
        
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].asunto, "Reunion Urgente")

    def test_mover_mensaje_entre_carpetas(self):
        """
        Prueba el requisito de mover mensajes entre carpetas (Entrega 2).
        Simula mover de 'Bandeja de Entrada' a 'Trabajo'.
        """
        msg = Mensaje("cliente@mail.com", "yo@mail.com", "Presupuesto", "...")
        
        # 1. Llega a bandeja de entrada
        self.raiz.agregar_mensaje(msg)
        self.assertIn(msg, self.raiz.mensajes)
        
        # 2. Operación de Mover: Eliminar de Origen -> Agregar a Destino
        self.raiz.eliminar_mensaje(msg)
        self.sub_trabajo.agregar_mensaje(msg)
        
        # 3. Validaciones
        self.assertNotIn(msg, self.raiz.mensajes)      # No está en origen
        self.assertIn(msg, self.sub_trabajo.mensajes)  # Está en destino

    def test_busqueda_sin_resultados(self):
        """Verifica caso borde: búsqueda sin coincidencias"""
        resultados = self.raiz.buscar_mensajes_recursivo("Inexistente")
        self.assertEqual(resultados, [])

if __name__ == '__main__':
    unittest.main()