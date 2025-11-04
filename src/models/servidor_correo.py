import networkx as nx 
from src.models.mensaje import Mensaje

class ServidorCorreo:
    def __init__(self):
        self._usuarios = {}
        self._red_servidores = nx.DiGraph() 

    def agregar_servidor(self, nombre_servidor):
        """Agrega un nodo (servidor) al grafo si no existe."""
        if nombre_servidor and nombre_servidor not in self._red_servidores:
            self._red_servidores.add_node(nombre_servidor)

    def agregar_conexion(self, origen, destino):
        """Agrega una arista dirigida entre dos servidores (conexión de envío)."""
        self.agregar_servidor(origen)
        self.agregar_servidor(destino)
        self._red_servidores.add_edge(origen, destino, weight=1) 

    def buscar_conectividad_dfs(self, origen, destino):
        """Verifica si existe un camino (conectividad) usando un algoritmo basado en DFS."""
        try:
            return nx.has_path(self._red_servidores, origen, destino)
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            return False

    def enviar_mensaje(self, mensaje):
        """Simula el envío. Si el destinatario es local, entrega. Si es externo, usa el grafo (BFS)."""
        
        destinatario = self._usuarios.get(mensaje.destinatario)
        if destinatario:
            destinatario.carpetas[0].agregar_mensaje(mensaje)
            return True
        else:
            remitente_servidor = mensaje.remitente.split('@')[-1]
            destino_servidor = mensaje.destinatario.split('@')[-1]

            self.agregar_servidor(destino_servidor)

            try:
                ruta_bfs = nx.shortest_path(
                    self._red_servidores, 
                    source=remitente_servidor, 
                    target=destino_servidor
                )
                print(f"📡 Ruta de envío (BFS, camino más corto): {' -> '.join(ruta_bfs)}")
                return True 
            except nx.NetworkXNoPath:
                print(f"❌ Error: No se encontró una ruta de {remitente_servidor} a {destino_servidor}.")
                return False
            except nx.NodeNotFound as e:
                print(f"❌ Error: Uno o ambos servidores no existen en la red: {e}")
                return False

    def listar_usuarios(self):
        return list(self._usuarios.keys())

    def registrar_usuario(self, usuario):
        self._usuarios[usuario.correo] = usuario
        dominio = usuario.correo.split('@')[-1]
        self.agregar_servidor(dominio)