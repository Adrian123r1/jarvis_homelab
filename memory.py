#!/usr/bin/env python3
import subprocess
import logging
import os

# Asegura que la carpeta exista y guarda el log en la ruta exacta que te pidieron
log_path = os.path.expanduser("~/jarvis_homelab/memory.log")
os.makedirs(os.path.dirname(log_path), exist_ok=True)

logging.basicConfig(
    filename=log_path,
    level=logging.INFO, 
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# ═══ BLOQUE 1: CAPTURAR (sensores) ═══
def capturar():
    salida = subprocess.check_output(["free", "-m"]).decode("utf-8")
    return salida

# ═══ BLOQUE 2: TRANSFORMAR (cerebro) ═══
def transformar(salida):
    lineas = salida.split("\n")
    campos = lineas[1].split()
    disponible = int(campos[6])
    return disponible

# ═══ BLOQUE 3: REPORTAR (voz) ═══
def reportar(disponible):
    if disponible < 500:
        logging.warning(f"LOW MEMORY: only {disponible} MB available")
    else:
        logging.info(f"Memory OK: {disponible} MB available")

# ═══ EJECUCIÓN ═══
salida = capturar()
disponible = transformar(salida)
reportar(disponible)

