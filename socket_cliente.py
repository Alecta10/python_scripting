import socket
import os
from dotenv import load_dotenv
from pathlib import Path

# Cargar variables de entorno desde el archivo .env
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

socket_ip = os.getenv('SOCKET_CLIENT_IP')
puerto_socket = int(os.getenv('PUERTO_SOCKET'))
archivo = 'rockyou.txt'

# AF_INET es para utilizar ipv4
# SOCK_STREAM es para utilizar protocolo tcp
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conexion:
    conexion.connect((socket_ip, puerto_socket))
    with open(archivo, 'rb') as archivo_binario:
        data = archivo_binario.read(1024)
        conexion.sendall(data)
        print("Archivo enviado")