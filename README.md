# 🧹 Colección de Programas para Linux

Colección oficial de mis scripts y herramientas de automatización en Python destinadas a la facilitación de tareas para usuarios con sistemas Linux.

---

## 🚀 Herramienta 1: Optimizador Universal (`mantenimiento.py`)

Un limpiador automático del sistema que elimina la basura del disco duro y libera la memoria RAM.

### 📋 Requisitos previos
Para que este script pueda enviar las órdenes de limpieza al sistema operativo, necesitas tener instalada la herramienta `apt` (como en Ubuntu, ZorinOS o Linux Mint).

### 🛠️ Cómo ejecutar el programa
1. Abre tu terminal de Linux.
2. Viaja a la carpeta donde está el archivo.
3. Ejecuta el script con el comando:
   ```bash
   python3 mantenimiento.py
   ```

### ⚙️ Opciones disponibles
* **Opción 1 (Limpiar caché):** Ejecuta una orden profunda al Kernel de Linux para vaciar la memoria RAM libre de restos de programas cerrados.
* **Opción 2 (Optimización total):** Busca y elimina del disco duro los paquetes de software huérfanos (`autoremove`) y los instaladores antiguos obsoletos (`autoclean`).

---
*Desarrollado con orgullo por **LucScript** 🐧🔥*
