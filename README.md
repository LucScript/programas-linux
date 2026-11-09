# 🧹 Colección de Programas para Linux

Colección oficial de mis scripts y herramientas de automatización en Python destinadas a mejorar el rendimiento, ahorrar recursos y facilitar tareas en sistemas **Linux**.

---

## 📁 Sección: Optimización del Sistema

Dentro de la carpeta `Optimización_del_Sistema` encontrarás dos variantes diseñadas para adaptarse a lo que necesites en cada momento:

### 1. ⚡ Versión Ligera (`cleaner.py`)
Un limpiador rápido e inmune a errores de entrada, ideal para liberar espacio de forma inmediata.
* **Opción 1 (Limpiar caché):** Vacía la memoria RAM libre de restos de programas cerrados.
* **Opción 2 (Optimización total):** Elimina paquetes de software huérfanos (`autoremove`) y limpiadores antiguos (`autoclean`).

### 2. 🚀 Versión Completa (`mantenimiento.py`)
El panel de control integral. **Incluye todas las opciones de la versión ligera** más 4 herramientas avanzadas:
* **Opción 3:** Actualiza el sistema y todas tus aplicaciones de golpe.
* **Opción 4:** Muestra una tabla limpia con los Gigas libres de tu disco duro real.
* **Opción 5:** Abre el monitor de rendimiento interactivo en tiempo real (`btop`).
* **Opción 6:** Ejecuta un test de velocidad real de tu línea de internet (`speedtest`).

---

## 🛠️ Cómo instalar y usar (¡Crea tu acceso rápido!)

### Paso 1: Instalar las herramientas extra (Obligatorio para la Versión Completa)
Abre tu terminal de Linux y ejecuta este comando para que funcionen el monitor y el test de velocidad:
```bash
sudo apt install btop speedtest-cli -y
```

### Paso 2: Crear el Alias Permanente (Recomendado ⭐)
Para no tener que buscar carpetas ni escribir rutas largas cada vez, crea un comando rápido en tu terminal. Sustituye `ruta/de/tu/archivo` por la ubicación donde hayas guardado el script:
```bash
echo "alias cleaner='python3 ~/ruta/de/tu/mantenimiento.py'" >> ~/.bashrc && source ~/.bashrc
```
* **¡A disfrutar!** A partir de este momento, escribe solo **`cleaner`** en cualquier ventana de la terminal y el programa arrancará al instante. *(Siéntete libre de cambiar la palabra `cleaner` en el comando por el nombre que te sea más cómodo).*

### Paso 3: Ejecución manual (Opcional)
Si prefieres no crear un alias, entra en la carpeta donde descargaste el archivo y ejecútalo de forma tradicional:
```bash
python3 mantenimiento.py
```

---
*Desarrollado con orgullo por **LucScript** 🐧🔥*
