from src.models.usuario import Usuario
from src.models.mensaje import Mensaje
from src.models.carpeta import Carpeta
from src.models.servidor_correo import ServidorCorreo

def iniciar_app():
    servidor = ServidorCorreo()

    servidor.agregar_servidor("mi_empresa.com")
    servidor.agregar_servidor("gmail.com")
    servidor.agregar_servidor("yahoo.com")
    servidor.agregar_servidor("servidor_intermedio.net")
    
    servidor.agregar_conexion("mi_empresa.com", "servidor_intermedio.net")
    servidor.agregar_conexion("servidor_intermedio.net", "gmail.com")
    servidor.agregar_conexion("servidor_intermedio.net", "yahoo.com")
    servidor.agregar_conexion("gmail.com", "mi_empresa.com")
    servidor.agregar_conexion("mi_empresa.com", "yahoo.com") 

    print("📬 Bienvenido al Cliente de Correo")
    usuario = crear_usuario()
    servidor.registrar_usuario(usuario)
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
        print("7. Salir") 

        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            print(f"\nUsuario: {usuario.nombre} - {usuario.correo}")
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
    mensajes = usuario.carpetas[0].listar_mensajes()
    if not mensajes:
        print("No hay mensajes.")
    else:
        for i, m in enumerate(mensajes, 1):
            estado = "📖" if m.leido else "📩"
            print(f"{i}. {estado} De: {m.remitente} | Asunto: {m.asunto}")
        input("Presioná Enter para marcar todos como leídos.")
        for m in mensajes:
            m.marcar_leido()

def filtrar_mensajes(usuario):
    palabra = input("🔍 Palabra clave en el asunto: ").lower()
    mensajes = usuario.carpetas[0].listar_mensajes()
    filtrados = [m for m in mensajes if palabra in m.asunto.lower()]
    print(f"\n🔎 Mensajes que contienen '{palabra}':")
    for i, m in enumerate(filtrados, 1):
        print(f"{i}. De: {m.remitente} | Asunto: {m.asunto}")

def simular_envio_servidores(servidor):
    print("\n--- SIMULACIÓN DE RUTA DE CORREO (BFS/DFS) ---")
    print("Servidores de ejemplo: mi_empresa.com, gmail.com, yahoo.com, servidor_intermedio.net")
    origen = input("Servidor de Origen: ")
    destino = input("Servidor de Destino: ")
    
    mensaje_simulado = Mensaje(f"simulado@{origen}", f"simulado@{destino}", "Simulación", "Ruta")
    
    print("\n--- RESULTADO DEL ENVÍO (Lógica BFS) ---")
    if servidor.enviar_mensaje(mensaje_simulado):
        print("✅ Simulación exitosa.")
    else:
        print("❌ Simulación fallida. Mensaje no pudo ser enrutado.")

    conectado = servidor.buscar_conectividad_dfs(origen, destino)
    print(f"\n🔗 Verificación de Conectividad (Lógica DFS): {'SÍ hay un camino' if conectado else 'NO hay un camino'}")