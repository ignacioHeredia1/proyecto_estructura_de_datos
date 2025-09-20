# 📄 Documentación Técnica – Entrega 1

## 🧠 Proyecto: Cliente de Correo en Python

### 👥 Integrantes del grupo
- Ignacio Heredia
- [Nombre del compañero 1]
- [Nombre del compañero 2]

### 🎯 Objetivo
Desarrollar un sistema de correo electrónico básico en consola, aplicando programación orientada a objetos y estructuras dinámicas. El sistema permite crear usuarios, enviar mensajes simulados, organizar correos en carpetas y filtrarlos por asunto.

---

## 🧱 Estructura del Proyecto

proyecto_estructura_de_datos/ 
├── src/ 
│ ├── main.py 
│ ├── models/ 
│ │ ├── usuario.py 
│ │ ├── mensaje.py 
│ │ ├── carpeta.py 
│ │ └── init.py 
│ └── interface/ 
│ └── cli_interface.py 
├── tests/ 
│ ├── test_import.py 
│ ├── tests_usuario.py 
│ └── init.py 
├── docs/ 
│ └── entrega_1/ 
│ └── documentacion_entrega_1.md 
├── README.md 
└── requirements.txt

---

## 🧩 Clases principales

### `Usuario`
- Atributos: nombre, correo, contraseña, carpetas
- Métodos: agregar_carpeta()

### `Mensaje`
- Atributos: remitente, destinatario, asunto, cuerpo, leído
- Métodos: marcar_leido()

### `Carpeta`
- Atributos: nombre, mensajes
- Métodos: agregar_mensaje(), listar_mensajes()

---

## 🖥️ Interfaz

El archivo `cli_interface.py` contiene un menú interactivo que permite al usuario:

- Crear su cuenta
- Enviar mensajes
- Ver bandeja de entrada
- Filtrar mensajes por asunto
- Salir del sistema

---

## ▶️ Ejecución

Desde la raíz del proyecto:

```bash
python -B -m src.main


