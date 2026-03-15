import threading

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

def tarea1():
    for i1 in numeros:
        print("Soy el hilo1 y i = ", i1)

def tarea2():
    for i2 in numeros:
        print("Soy el hilo2 y i = ", i2)

def tarea3():
    for i3 in numeros:
        print("Soy el hilo3 y i = ", i3)

# Creacion del hilo
hilo1 = threading.Thread(target= tarea1)
hilo2 = threading.Thread(target= tarea2)
hilo3 = threading.Thread(target= tarea3)

# Inicializacion de los hilos
hilo1.start()
hilo2.start()
hilo3.start()

# Con join se espera a que termine el hilo
hilo1.join()
hilo2.join()
hilo3.join()
print("Todos los hilos han finalizados")