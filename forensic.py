#!/usr/bin/env python3
# ═══ IMPORTS ═══
import logging
import os

# Preparación del taller
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# ═══ BLOQUE 1: CAPTURAR (sensores) ═══
def capturar_archivo_log():
    log_path = os.path.expanduser("~/jarvis_homelab/security_breach.log")
    # Abrimos el archivo directamente en Python para leer sus líneas
    with open(log_path, "r", encoding="utf-8") as f:
        lineas = f.read().splitlines()
    return lineas

# ═══ BLOQUE 2: TRANSFORMAR (cerebro) ═══
def transformar_usuarios(lineas):
    lista_intrusos = []
    for linea in lineas:
        if not linea.strip():
            continue
        campos = linea.split()
        usuario_ficha = {
            "user": campos[0],
            "terminal": campos[1],
            "since": f"{campos[2]} {campos[3]}",
        }
        lista_intrusos.append(usuario_ficha)
    return lista_intrusos

# ═══ BLOQUE 3: REPORTAR (voz) ═══
def reportar_intrusiones(lista_usuarios):
    for usuario in lista_usuarios:
        if usuario["user"] != "adrian":
            logging.warning(f"UNAUTHORIZED USER DETECTED: {usuario['user']} on {usuario['terminal']} since {usuario['since']}")
        else:
            logging.info(f"Authorized user: adrian on {usuario['terminal']}")

# ═══ EJECUCIÓN ═══
lineas_evidencia = capturar_archivo_log()
usuarios_procesados = transformar_usuarios(lineas_evidencia)
reportar_intrusiones(usuarios_procesados)
