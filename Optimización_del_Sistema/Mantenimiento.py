import os
import sys

def lucscript_linuxcleaner():
    print("🧹 -- LUCSCRIPT LINUX CLEANER -- 🧹\n\n1. Limpiar caché\n2. Optimización total\n3. Actualizar el sistema\n4. Espacio en disco\n5.Gestión de procesos en segundo plano\n6. Revisar velocidad de conexión")
    option = input("Escribe el número de la opción: ")

    if option == "1":
        print("Borrando la memoria caché del sistema...")
        os.system("sync && sudo sysctl -w vm.drop_caches=3")
    elif option == "2":
        print("Eliminando paquetes obsoletos y limpiando el disco...")
        os.system("sudo apt remove -y && sudo apt autoclean")
    elif option == "3":
        print("Actualizando el sistema...")
        os.system("sudo apt update && sudo apt upgrade -y")
    elif option == "4":
        print("Calculando el espacio libre en el disco...")
        os.system("df -h --output=source,size,used,avail,pcent,target -x tmpfs -x devtmpfs")
    elif option == "5":
        print("Cargando programas en segundo plano...")
        os.system("btop")
    elif option == "6":
        print("🌐Iniciando test de velocidad de internet...")
        print("Conectando con el servidor más cercano (esto puede tardar unos segundos)...")
        os.system("speedtest --simple")
    else:
        print("Opción seleccionada no válida")
lucscript_linuxcleaner()