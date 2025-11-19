from src.models.usuario import Usuario
from src.models.mensaje import Mensaje
from src.models.carpeta import Carpeta
from src.models.servidor_correo import ServidorCorreo

def iniciar_app():
    servidor = ServidorCorreo()

    # --- PRE-CARGA DE DATOS (Para probar la red de servidores) ---
    servidor.agregar_servidor("mi_empresa.com")
    servidor.agregar_servidor("gmail.com")
    servidor.agregar_servidor("yahoo.com")
    servidor.agregar_servidor("servidor_intermedio.net")
    
    # Definimos las rutas (Aristas del Grafo)
    servidor.agregar_conexion("mi_empresa.com", "servidor_intermedio.net")
    servidor.agregar_conexion("servidor_intermedio.net", "gmail.com")
    servidor.agregar_conexion("servidor_intermedio.net", "yahoo.com")
    servidor.agregar_conexion("gmail.com", "mi_empresa.com")
    servidor.agregar_conexion("mi_empresa.com", "yahoo.com") 

    print("📬 Bienvenido al Cliente de Correo")
    usuario = crear_usuario()
    servidor.registrar_usuario(usuario)
    
    # Inicialización de carpetas base
    bandeja = Carpeta("Bandeja de entrada")
    usuario.agregar_carpeta(bandeja)

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ver información del usuario")
        print("2. Enviar mensaje")
        print("3. Ver bandeja de entrada")
        print("4. Filtrar mensajes por asunto")
        print("5. Ver usuarios registrados")
        print("6. Simular envío por red de servidores (BFS/DFS)") 
        print("7. Configuración de Perfil (Setters)") # <--- NUEVA OPCIÓN
        print("8. Salir") 

        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            print(f"\nUsuario: {usuario.nombre} | Correo: {usuario.correo}")
        elif opcion == "2":
            enviar_mensaje(usuario, servidor)
        elif opcion == "3":
            mostrar_bandeja(usuario)
        elif opcion == "4":
            filtrar_mensajes(usuario)
        elif opcion == "5":
            print("\n📋 Usuarios registrados:")
            for correo in servidor.listar_usuarios():
                print(f"- {correo}")
        elif opcion == "6":
            simular_envio_servidores(servidor)
        elif opcion == "7":
            menu_configuracion(usuario, servidor) # <--- LLAMA AL SUB-MENÚ
        elif opcion == "8":
            print("👋 Cerrando sesión. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Probá de nuevo.")

def crear_usuario():
    print("\n--- CREAR USUARIO ---")
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    contraseña = input("Contraseña: ")
    return Usuario(nombre, correo, contraseña)

def enviar_mensaje(usuario, servidor):
    print("\n--- ENVIAR MENSAJE ---")
    destinatario = input("Para (correo): ")
    asunto = input("Asunto: ")
    cuerpo = input("Mensaje: ")
    mensaje = Mensaje(usuario.correo, destinatario, asunto, cuerpo)
    
    print("\n--- RESULTADO DEL ENVÍO ---")
    if servidor.enviar_mensaje(mensaje):
        print("✅ Mensaje entregado.")
    else:
        print("❌ Fallo en el envío. No hay ruta o servidor no existe.")

def mostrar_bandeja(usuario):
    print("\n📥 Bandeja de entrada:")
    if not usuario.carpetas:
        print("No hay carpetas configuradas.")
        return

    mensajes = usuario.carpetas[0].listar_mensajes()
    if not mensajes:
        print("No hay mensajes.")
    else:
        for i, m in enumerate(mensajes, 1):
            estado = "📖" if m.leido else "📩"
            print(f"{i}. {estado} De: {m.remitente} | Asunto: {m.asunto} | Mensaje: {m.cuerpo}")
        
        marcar = input("\n¿Marcar todos como leídos? (s/n): ")
        if marcar.lower() == 's':
            for m in mensajes:
                m.marcar_leido()
            print("Mensajes marcados como leídos.")

def filtrar_mensajes(usuario):
    if not usuario.carpetas:
        print("No hay carpetas para buscar.")
        return

    palabra = input("🔍 Palabra clave en el asunto: ").lower()
    mensajes = usuario.carpetas[0].listar_mensajes()
    filtrados = [m for m in mensajes if palabra in m.asunto.lower()]
    
    print(f"\n🔎 Mensajes que contienen '{palabra}':")
    if not filtrados:
        print("No se encontraron coincidencias.")
    else:
        for i, m in enumerate(filtrados, 1):
            print(f"{i}. De: {m.remitente} | Asunto: {m.asunto}")

def simular_envio_servidores(servidor):
    print("\n--- SIMULACIÓN DE RUTA DE CORREO (BFS/DFS) ---")
    print("Servidores disponibles: mi_empresa.com, gmail.com, yahoo.com, servidor_intermedio.net")
    
    origen = input("Servidor de Origen (ej: gmail.com): ")
    destino = input("Servidor de Destino (ej: yahoo.com): ")
    
    mensaje_simulado = Mensaje(f"test@{origen}", f"test@{destino}", "Test de Ruta", "Probando grafos")
    
    print(f"\n📡 Intentando enviar de {origen} a {destino}...")
    
    print("\n--- RESULTADO BFS (Camino Corto) ---")
    if servidor.enviar_mensaje(mensaje_simulado):
        print("✅ Envío exitoso.")
    else:
        print("❌ No se pudo enviar el mensaje.")

    print("\n--- RESULTADO DFS (Verificar Conexión) ---")
    conectado = servidor.buscar_conectividad_dfs(origen, destino)
    if conectado:
        print("🔗 SÍ existe conectividad entre los servidores.")
    else:
        print("🚫 NO hay camino posible.")

# --- NUEVA LÓGICA PARA SETTERS ---
def menu_configuracion(usuario, servidor):
    """
    Sub-menú para probar los SETTERS de la clase Usuario.
    Permite cambiar nombre, correo y contraseña.
    """
    while True:
        print("\n--- ⚙️ CONFIGURACIÓN DE PERFIL ---")
        print(f"Datos actuales: {usuario.nombre} | {usuario.correo}")
        print("1. Cambiar Nombre")
        print("2. Cambiar Contraseña")
        print("3. Cambiar Correo")
        print("4. Volver al menú principal")
        
        opcion = input("¿Qué querés modificar?: ")

        if opcion == "1":
            nuevo = input("Nuevo nombre: ")
            if nuevo:
                usuario.nombre = nuevo # Usa el Setter @nombre.setter
                print("✅ Nombre actualizado.")
        
        elif opcion == "2":
            nuevo = input("Nueva contraseña: ")
            if nuevo:
                usuario.contraseña = nuevo # Usa el Setter @contraseña.setter
                print("✅ Contraseña actualizada.")
        
        elif opcion == "3":
            print("⚠️ Atención: Al cambiar el correo, debés avisar al servidor.")
            nuevo = input("Nuevo correo: ")
            if nuevo:
                # Actualizamos el objeto Usuario (Setter)
                usuario.correo = nuevo 
                # Actualizamos el registro en el servidor para que sigan llegando mensajes
                servidor.registrar_usuario(usuario)
                print("✅ Correo actualizado y registrado.")
        
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")