import requests
from bs4 import BeautifulSoup

url = 'http://escolares.dl/wordpress/wp-login.php'

usuario = 'luisillo'
password = 'Luis1981'

cabecera = {
    "Host": "escolares.dl",
    "Content-Length": "112",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "http://escolares.dl",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "http://escolares.dl/wordpress/wp-login.php",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "es-ES,es;q=0.9",
    "Cookie": "wordpress_test_cookie=WP%20Cookie%20check",
    "Connection": "close"
}

payload = {
    'log' : usuario,
    'pwd' : password,
    'wp-submit' : 'Acceder',
    'redirect_to' : 'http://escolares.dl/wordpress/wp-login.php',
    'testcookie' : '1'
}

with requests.Session() as sesion:
    sesion.get(url, headers=cabecera)
    respuesta = sesion.post(url, headers=cabecera, data=payload, allow_redirects=True)
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    error_mensaje = soup.find('div', {'id' : 'login_error'})
    print(f"Intentando inicar sesion con {usuario} y {password}")

    if error_mensaje:
        print("No se ha realizado el login")
        exit()

    else:
        print("Inicio de sesión satisfactorio")
        exit()
