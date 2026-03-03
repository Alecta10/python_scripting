import os
import zipfile
import paramiko
from dotenv import load_dotenv
from pathlib import Path
from scp import SCPClient, SCPException

lista_extension = ('.pdf', 'txt', '.doc')
archivo_zip = 'archivo.zip'

# función para comprimir archivos con las extensiones especificadas en un archivo zip
def to_zip():
    with zipfile.ZipFile(archivo_zip, 'w') as zipf:
        for archivo in os.listdir():
            if archivo.endswith(lista_extension):
                zipf.write(archivo)

try:
    env_path = Path(__file__).parent / ".env"
    load_dotenv(dotenv_path=env_path)

    ssh_ip_host = os.getenv('IP_HOST_SSH')
    ssh_user = os.getenv('SSH_USER')
    ssh_passwd = os.getenv('SSH_PASSWD')
    ssh_port = os.getenv('SSH_PORT')

    # Crear un cliente SSH con paramiko
    cliente = paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Cargar las claves de host conocidas para evitar advertencias de seguridad
    try:
        cliente.load_system_host_keys() # Es mejor que poner la ruta a mano

    except IOError:
        print("Archivo known_hosts no encontrado, se creará uno nuevo.")

    # Conectar al servidor SSH
    cliente.connect(ssh_ip_host, port=ssh_port, username=ssh_user, password=ssh_passwd)
    print("Conexión SSH establecida con éxito.")

    # Ejecutar un comando en el servidor remoto
    # Cada stdin, stdout, stderr es un objeto de tipo file-like que se puede leer o escribir
    stdin, stdout, stderr = cliente.exec_command("ls -l")
    
    resultado = stdout.read().decode() 
    print("Resultado del comando 'ls -l':")
    print(resultado)

    to_zip()

    # Usar SCP para subir un archivo al servidor remoto
    with SCPClient(cliente.get_transport()) as scp_enviar:
        scp_enviar.put(archivo_zip, "subir_remoto.zip")
        print("Archivo subido con éxito.")

    # Usar SCP para descargar un archivo del servidor remoto
    with SCPClient(cliente.get_transport()) as scp_descargar:
        scp_descargar.get("descargar_remoto.txt", "descargar_local.txt")
        print("Archivo descargado con éxito.")

except Exception as e:
    print("Error al conectar por SSH:", e)

finally:
    # Siempre cerrar la conexión SSH al finalizar
    cliente.close()
