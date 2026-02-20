import mysql.connector
import os
import re
from enum import Enum
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

# Enum para definir los tipos de consulta
class TipoConsulta(Enum):
    NOMBRES = 1
    EMAILS = 2
    TODO = 3

def obtener_conexion():
    print("Conexión abierta con éxito")  
    
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DATABASE'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        auth_plugin='mysql_native_password'
    )

#
def es_email_valido(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None

def insertar_usuario(nombre, email):
    print(f"{nombre} - {email} ")

    # Validar que el nombre no esté vacío y que el email tenga un formato válido
    if not nombre or not es_email_valido(email):
        return False, "Datos inválidos o email incorrecto"
    
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        query = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
        cursor.execute(query, (nombre, email))
        conn.commit()
        conn.close()
        return True, f"Agregado: {nombre}"
    
    except Exception as e:
        return False, str(e)
    
def consultar_datos(tipo):
    datos = []
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        
        # Dependiendo del tipo de consulta, se ejecuta una consulta SQL diferente
        if tipo == TipoConsulta.NOMBRES:
            cursor.execute('SELECT nombre FROM usuarios')
            datos = [f"Nombre: {f[0]}" for f in cursor.fetchall()]

        elif tipo == TipoConsulta.EMAILS:
            cursor.execute('SELECT email FROM usuarios')
            datos = [f"Email: {f[0]}" for f in cursor.fetchall()]

        elif tipo == TipoConsulta.TODO:
            cursor.execute('SELECT * FROM usuarios')
            datos = [f"ID: {f[0]}, Nom: {f[1]}, Email: {f[2]}" for f in cursor.fetchall()]

    except mysql.connector.Error as error:
        print("Error al conectar a MySQL:", error)

    # Asegurarse de cerrar la conexión incluso si ocurre un error
    finally:
        if conn and conn.is_connected():
            conn.close()
            print("Conexión cerrada")  

    return datos