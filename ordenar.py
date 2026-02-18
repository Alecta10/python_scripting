import os
import shutil

categorias = {
    'ejecutables': ('.py', '.sh', '.exe'),
    'documentos': ('.txt', '.pdf', '.docx'),
    'fotos': ('.png', '.jpg', '.jpeg', '.gif'),
    'videos': ('.mp4', '.avi', '.mkv'),
    'musica': ('.mp3', '.wav', '.flac')
}

# Obtener el nombre del script actual para evitar moverlo
nombre_script = os.path.basename(__file__)

for archivo in os.listdir():
    #switch para copiar archivos .py
    # Saltamos las carpetas y el propio script para que no den error al intentar moverlo
    if os.path.isdir(archivo) or archivo == nombre_script:
        continue

    for carpeta, extensiones in categorias.items():
        if archivo.endswith(extensiones):
            if not os.path.exists(carpeta):
                os.makedirs(carpeta) # Crea la carpeta si no existe
                
            shutil.move(archivo, carpeta + '/' + archivo) # Mueve el archivo a cada carpeta según su categoría
            print(f"Se ha movido el archivo: {archivo} a la carpeta {carpeta}")
            break

   

