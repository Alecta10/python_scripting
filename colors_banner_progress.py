from colorama import Fore, Back, Style
from tqdm import tqdm
import os
import time

def fuerza_bruta_ej():
    ruta_archivo = "rockyou.txt"
    total_lineas = 14344392
        
    os.system('clear')
    print(Back.MAGENTA + "  SISTEMA DE CRACKING ACTIVO CON TQDM  " + Style.RESET_ALL)
    print("\n" * 1) 

    try:
        # el encoding para que pueda leer bien la ñ y mas caracteres
        with open(ruta_archivo, 'r', encoding='latin-1') as file:
            # tqdm es la libreria para la progress bar
            # el ncols es para el tamaño maximo
            pbar = tqdm(file, total=total_lineas, ncols=100)
            for linea in pbar:
                raw_password = linea.strip()
                # Cuando encuentra un caracter que no se puede imprimir
                # no lo imprime porque hace que se descuadre el print
                # es un filtro que recorre la palabra entera en busqueda 
                # de algo que lo descuadre como saltos de lineas
                password = "".join(c for c in raw_password if c.isprintable())
                
                # Primero ponemos los colores despues la contraseña si mide mas de 20 se imprime cortado
                # para que no se mueva todo el print y solo se vea cambiando las contraseñas y por ultimo
                # el reseteo de los colores
                pbar.set_description(f"Probando: {Fore.YELLOW}{password[:20]:<20}{Style.RESET_ALL}")

    except FileNotFoundError:
        print(f"\n{Fore.RED}Error: rockyou.txt no encontrado.")

# se indica 'r' porque se imprime tal cual es, en raw
print(Back.MAGENTA + r"""
..####...##......######..##..##.
.##..##..##......##.......####..
.######..##......####......##...
.##..##..##......##.......####..
.##..##..######..######..##..##.
................................
""" + Style.RESET_ALL)

time.sleep(0.5)

print(Fore.RED + 'Este texto es rojo')
print(Style.RESET_ALL + 'Reiniciamos color')
print(Back.GREEN + 'Este texto tiene un fondo verde')
print(Style.RESET_ALL + 'Reiniciamos color')
print(Style.BRIGHT + 'Este texto es brillante')
print(Style.RESET_ALL + 'Reiniciamos color')
print(Style.BRIGHT + Fore.YELLOW + 'Este es un texto en amarillo brillante (amarillo fosforito)')
print(Style.RESET_ALL + 'Reiniciamos color')
print(Fore.YELLOW + 'Este es un texto en amarillo')


print(Fore.RED + 'Texto en rojo')
print(Style.RESET_ALL + 'Reiniciamos color')
print(Fore.GREEN + 'Texto en verde')
print(Style.RESET_ALL + 'Reiniciamos color')
print(Fore.BLUE + 'Texto en azul')
print(Style.RESET_ALL + 'Reiniciamos color')

print(Back.YELLOW + 'Fondo amarillo')
print(Style.RESET_ALL + 'Reiniciamos color')
print(Back.MAGENTA + 'Fondo magenta')
print(Style.RESET_ALL + 'Reiniciamos color')


print(Style.DIM + 'Texto tenue')
print(Style.RESET_ALL + 'Reiniciamos color')
print(Style.NORMAL + 'Texto normal')
print(Style.RESET_ALL + 'Reiniciamos color')
print(Style.BRIGHT + 'Texto brillante')
print(Style.RESET_ALL + 'Reiniciamos color')

time.sleep(1)
fuerza_bruta_ej()

