from src.models.usuario import Usuario
from src.models.mensaje import Mensaje
from src.models.carpeta import Carpeta
from src.models.servidor_correo import ServidorCorreo
from src.controllers.email_controller import EmailController
from src.controllers.filtro_controller import FiltroController

def iniciar_app():
    servidor = ServidorCorreo()
    controlador = EmailController()
    filtro = FiltroController()

    print("📬 Bienvenido al Cliente de Correo")
    usuario = crear_usuario()
    servidor.registrar_usuario(usuario)

    bandeja = Carpeta("Bandeja de entrada")
    importante = Carpeta("Importante")
    usuario.agregar_carpeta(bandeja)
    usuario.agregar_carpeta(importante)

    subcarpeta = Carpeta("Subcarpeta de pruebas")
    importante.agregar_subcarpeta(subcarpeta)

    filtro.agregar_regla("urgente", importante)

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ver información del usuario")
        print("2. Enviar mensaje")
        print("3. Ver bandeja de entrada")
        print("4. Buscar mensaje (recursivo)")
        print("5. Mover mensaje a otra carpeta")
        print("6. Ver estructura de carpetas")
        print("7. Ver mensajes urgentes")
        print("8. Ver usuarios registrados")
        print("9. Salir")

        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            print(f"\nUsuario: {usuario.nombre} - {usuario.correo}")
        elif opcion == "2":
            enviar_mensaje(usuario, servidor, controlador, filtro)
        elif opcion == "3":
            mostrar_bandeja(usuario)
        elif opcion == "4":
            buscar_mensaje(usuario)
        elif opcion == "5":
            mover_mensaje(usuario)
        elif opcion == "6":
            ver_estructura(usuario)
        elif opcion == "7":
            mostrar_urgentes(filtro)
        elif opcion == "8":
            print("\n📋 Usuarios registrados:")
            for correo in servidor.listar_usuarios():
                print(f"- {correo}")
        elif opcion == "9":
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

def enviar_mensaje(usuario, servidor, controlador, filtro):
    print("\n--- ENVIAR MENSAJE ---")
    destinatario = input("Para (correo): ")
    asunto = input("Asunto: ")
    cuerpo = input("Mensaje: ")
    urgente = input("¿Es urgente? (s/n): ").lower() == "s"

    mensaje = Mensaje(usuario.correo, destinatario, asunto, cuerpo)

    destinatario_obj = servidor.obtener_usuario(destinatario)
    if not destinatario_obj:
        print("❌ Usuario destinatario no registrado.")
        return

    if not destinatario_obj.carpetas:
        print("❌ El destinatario no tiene carpetas configuradas.")
        return

    destinatario_obj.carpetas[0].agregar_mensaje(mensaje)
    print("✅ Mensaje entregado.")

    if urgente:
        filtro.marcar_urgente(mensaje)

    if not filtro.aplicar_filtros(mensaje):
        controlador.enviar_mensaje(usuario, destinatario_obj, asunto, cuerpo)

def mostrar_bandeja(usuario):
    print("\n📥 Bandeja de entrada:")
    mensajes = usuario.carpetas[0].listar_mensajes()
    if not mensajes:
        print("No hay mensajes.")
    else:
        for i, m in enumerate(mensajes, 1):
            if isinstance(m, Mensaje):
                estado = "📖" if m.leido else "📩"
                print(f"{i}. {estado} De: {m.remitente} | Asunto: {m.asunto}")
            else:
                print(f"{i}. ⚠️ Mensaje inválido: {m}")
        input("Presioná Enter para marcar todos como leídos.")
        for m in mensajes:
            if isinstance(m, Mensaje):
                m.marcar_leido()

def buscar_mensaje(usuario):
    print("\n--- BÚSQUEDA RECURSIVA ---")
    criterio = input("Buscar por 'asunto' o 'remitente': ").lower()
    valor = input("Texto a buscar: ").lower()
    print(f"\n🔎 Resultados para '{valor}' en {criterio}:")
    for carpeta in usuario.carpetas:
        resultados = carpeta.buscar_mensaje(criterio, valor)
        for i, m in enumerate(resultados, 1):
            print(f"{i}. De: {m.remitente} | Asunto: {m.asunto}")

def mover_mensaje(usuario):
    print("\n--- MOVER MENSAJE ---")
    asunto = input("Asunto del mensaje a mover: ").lower()
    origen = usuario.carpetas[0]
    destino = usuario.carpetas[1]
    for m in origen.mensajes:
        if asunto in m.asunto.lower():
            origen.mover_mensaje(m, destino)
            print("✅ Mensaje movido a carpeta 'Importante'.")
            return
    print("❌ No se encontró el mensaje.")

def ver_estructura(usuario):
    def recorrer(carpeta, nivel=0):
        print("  " * nivel + f"📁 {carpeta.nombre}")
        for m in carpeta.mensajes:
            print("  " * (nivel + 1) + f"📩 {m.asunto}")
        for sub in carpeta.subcarpetas:
            recorrer(sub, nivel + 1)
    print("\n📂 Estructura de carpetas:")
    for carpeta in usuario.carpetas:
        recorrer(carpeta)

def mostrar_urgentes(filtro):
    print("\n📛 Mensajes urgentes:")
    mensaje = filtro.obtener_mensaje_urgente()
    if mensaje:
        print(f"De: {mensaje.remitente} | Asunto: {mensaje.asunto}")
    else:
        print("No hay mensajes urgentes.")
