from hashlib import md5
from virus_total_apis import PublicApi
from dotenv import load_dotenv
from pathlib import Path
import os
import sys

# Uso de argumentos para abrir el archivo deseado
if len(sys.argv) < 2:
    print(f"Uso: python3 {sys.argv[0]} <ruta_del_archivo>")
    sys.exit(1)

# Cargar variables de entorno desde el archivo .env
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

# Recogemos la key y la insertamos en api
VIRUS_API_KEY = os.getenv('VIRUS_API_KEY')
api = PublicApi(VIRUS_API_KEY)
ruta_archivo = sys.argv[1]

# Se utiliza como rb porque se trata de un hash necesita ser visto como binario
with open(ruta_archivo, 'rb') as file:
    hash_archivo = md5(file.read()).hexdigest()

respuesta = api.get_file_report('hash_archivo')

# Prueba, este hash es de EICAR Test File 
# respuesta = api.get_file_report('44d88612fea8a8f36de82e1278abb02f')

if respuesta['response_code'] == 200:

    # Se utiliza el .get('results', 0) como acceso seguro
    # Si existe results en respuesta, te da el valor sino 0
    resultados = respuesta.get('results', 0)

    if resultados['response_code'] == 1:
        reportes = resultados.get('positives', 0)
        total = resultados.get('total', 0)
        
        if reportes > 0:
            print(f"Detectado por {reportes}/{total} motores.")
            
        else:
            print("Archivo limpio (0 detecciones en VirusTotal).")

    else:
        print(f"El archivo con hash {hash_archivo} no ha sido analizado nunca en VirusTotal.")
        
else:
    print("Error al hacer la peticion: ", respuesta['response_code'])