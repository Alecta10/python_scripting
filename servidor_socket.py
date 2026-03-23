import socket
import os
from dotenv import load_dotenv
from pathlib import Path

# Cargar variables de entorno desde el archivo .env
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

socket_ip = os.getenv('SOCKET_SERVER_IP')
puerto_socket = os.getenv('PUERTO_SOCKET')

# AF_INET es para utilizar ipv4
# SOCK_STREAM es para utilizar protocolo tcp
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conexion:
    
    conexion.bind((socket_ip, puerto_socket))
    conexion.listen()
    connect, address = conexion.accept()

    with connect:
        print("Conexion recibida: ", connect)

        with open('archivo_recibido.txt', 'wb') as archivo_recibido:
            data = connect.recv(1024)
            archivo_recibido.write(data)
            print("Archivo recibido correctamente")
