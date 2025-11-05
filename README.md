# 📧 Cliente de Correo Electrónico – Proyecto Final (Estructuras de Datos, UNaB)

## 👥 Integrantes
- Ariel Aguilar  
- Ignacio Nicolás Heredia  
- Katherine Avendaño  

---

## 📌 Descripción
Este proyecto implementa un **cliente de correo electrónico en Python** como trabajo final de la materia **Estructuras de Datos**.  
A lo largo de distintas entregas se aplicaron:
- **Programación Orientada a Objetos (POO)**  
- **Estructuras de datos**: árboles, listas, diccionarios, colas de prioridad, grafos  
- **Algoritmos**: recursividad, BFS y DFS  
- **Buenas prácticas**: modularidad, documentación, manejo de versiones  

---

## 🚀 Funcionalidades por entrega

🔹 Entrega 1 – Modelado de clases
Clases: Usuario, Mensaje, Carpeta, ServidorCorreo

Encapsulamiento con atributos privados y propiedades

Interfaces básicas para enviar y listar mensajes .

🔹 Entrega 2 – Estructuras de Datos y Recursividad
Gestión de carpetas y subcarpetas implementada como un Árbol General (clase Carpeta con _subcarpetas).

Implementación de búsqueda recursiva de mensajes por asunto o remitente (Carpeta.buscar_mensaje).

🔹 Entrega 3 – Algoritmos y Funcionalidades Avanzadas

Filtros automáticos: Uso de Diccionarios (filtro_controller.py) para organizar mensajes según reglas.


Cola de Prioridad: Implementación de heapq (filtro_controller.py) para gestionar mensajes marcados como "urgentes".

Red de Servidores (Grafos):

Modelado de la red de servidores como un Grafo Dirigido (usando networkx en servidor_correo.py).

Simulación de enrutamiento de mensajes entre servidores usando BFS (para encontrar el camino más corto) y DFS (para verificar conectividad).

### Documentos
-📄 [Propuesta de Proyecto 2da entrega](docs/Proyecto%20tp%20Segunda%20entrega%20.docx) 
-🖼 [Diagrama Árbol de Carpetas](docs/diagramas/Diagrama_UML_Entrega1.pdf) 
-📄 [Powerpoint explicativo 2da entrega](docs/Cliente%20de%20correo%20electrónico.pptx)
-🖼 [Video explicativo del árbol de carpeta](docs/video%20explicando%20carpetas%20del%20proyecto.mp4)
-🖼 [Video explicando los algoritmos y funcionalidades de la 3ra entrega](docs/algoritmos_y_funcionalidades.mp4)

## ▶️ Cómo ejecutar 
```bash
python -B -m src.main

