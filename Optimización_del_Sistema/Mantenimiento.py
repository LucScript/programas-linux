import os
import sys

def lucscript_linuxcleaner():
    print("🧹 -- LUCSCRIPT LINUX CLEANER -- 🧹\n\n1. Limpiar caché\n2. Optimización total")
    option = int(input("Escribe el número de la opción: "))

    if option == 1:
        print("Borrando la memoria caché del sistema...")
        os.system("sync && sudo sysctl -w vm.drop_caches=3")
    elif option == 2:
        print("Eliminando paquetes obsoletos y limpiando el disco...")
        os.system("sudo apt remove -y && sudo apt autoclean")
lucscript_linuxcleaner()