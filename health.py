import subprocess
import logging

# Configuración profesional: escribe directamente en el archivo health.log
logging.basicConfig(
    filename="health.log",
    level=logging.INFO, 
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logging.info("Iniciando la verificación del sistema de salud...")

# 1. Traemos los datos del disco y los decodificamos a texto legible
disk_output = subprocess.check_output(["df", "/"]).decode("utf-8")

# 2. Cortamos por líneas y luego por espacios para extraer el porcentaje
lines = disk_output.split("\n")
fields = lines[1].split()
disk_percent = int(fields[4].replace("%", ""))

# 3. Reportamos el estado normal usando INFO en el archivo de log
logging.info(f"Disk usage: {disk_percent}%")

# 4. Evaluamos si hay un peligro real usando WARNING
if disk_percent > 80:
    logging.warning("WARNING: Disk above 80%")

