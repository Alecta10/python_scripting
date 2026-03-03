import ftplib
import getpass
import zipfile
import os
from dotenv import load_dotenv
from pathlib import Path

# Cargar variables de entorno desde el archivo .env
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

lista_extension = ('.sh', '.py', '.log')
archivo_zip = 'archivo.zip'

# función para comprimir archivos con las extensiones especificadas en un archivo zip
def to_zip():
    with zipfile.ZipFile(archivo_zip, 'w') as zipf:
        for archivo in os.listdir():
            if archivo.endswith(lista_extension):
                zipf.write(archivo)

def main():
    ftp = None
    try:

        ip_host = os.getenv('IP_HOST')
        ftp_user = os.getenv('FTP_USER')
        ftp_passwd = os.getenv('FTP_PASSWD')

        # establecer conexión FTP
        ftp = ftplib.FTP(ip_host)
        ftp.login(user=ftp_user, passwd=ftp_passwd)
        print("Connected:", ftp.getwelcome())

        to_zip()

        # subir el archivo zip al servidor FTP
        with open(archivo_zip, 'rb') as file:
            ftp.storbinary(f'STOR {archivo_zip}', file)
            print("archivo subido correctamente")

    except ftplib.all_errors as e:
        print("FTP error:", e)

    finally:
        if ftp is not None:
            try:
                ftp.quit()
                print("Conexion cerrada.")

            except:
                ftp.close() # Force close if quit fails


if __name__ == "__main__":
    main()