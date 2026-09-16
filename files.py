#!/usr/bin/env python3
# ═══ IMPORTS ═══
import subprocess

# ═══ BLOQUE 1: CAPTURAR (sensores) ═══
def capturar_archivos():
    # Ejecuta 'ls' para listar los archivos actuales en la carpeta
    salida_cruda = subprocess.check_output(["ls"]).decode("utf-8")
    return salida_cruda

# ═══ BLOQUE 2: TRANSFORMAR (cerebro) ═══
# Llamamos a la función para tener el texto de los archivos
texto_archivos = capturar_archivos()

# Cortamos el texto por los espacios para meter cada archivo en una lista
lista_archivos = texto_archivos.split()

# Contamos cuántos elementos hay dentro de la lista usando len()
total_archivos = len(lista_archivos)

# ═══ BLOQUE 3: REPORTAR (voz) ═══
# Imprimimos el resultado directo en la terminal
print(f"Módulo JARVIS: Se encontraron {total_archivos} archivos en este directorio.")
