import requests
import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

ABUSEIP_API_KEY = os.getenv('ABUSEIP_API_KEY')
url = 'https://api.abuseipdb.com/api/v2/check'

lista_ip = []

# Abrimos la lista de ips para consultar en la api
with open('archivo_ips.txt', 'r') as archivo_ips:
    for each_ip in archivo_ips:
        # quitamos los espacios que pueden haber con strip
        lista_ip.append(each_ip.strip())

for ip_stripped in lista_ip:
    headers = {
        'Key' : ABUSEIP_API_KEY,
        'Accept' : 'application/json'
    } 

    parametros = {
        'ipAddress' : ip_stripped,
        'maxAgeInDays' : '90',
    }

    # Esta api no requiere ninguna libreria mas que requests
    respuesta = requests.get(url, headers=headers, params=parametros)
    respuesta_json = respuesta.json()

    respuesta_json_data = respuesta_json.get('data', {})
    ip = respuesta_json_data.get('ipAddress', 'desconocida')

    # Uso del get para redirigir el flujo en caso de error
    reportes = respuesta_json_data.get('totalReports', -1)

    # Como -1 solo puede ser inducido por el get se sabe que es un error al encontrar
    # este atributo como totalReports
    if reportes == -1:
        print("Hay un error al recoger totalReports en la api")
        print(respuesta_json)

    else:
        print(f"La ip {ip} tiene {reportes} reportes")