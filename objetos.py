import os
import shutil

class SistemaOperativo:
	# Definimos al constructor y atributos
	def __init__(self, nombre_archivo, nombre_carpeta, own):
		self.nombre_archivo = nombre_archivo
		self.nombre_carpeta = nombre_carpeta
		self.own = own
	
	# Definimos sus metodos
	def crear_carpeta(self):
		os.mkdir(self.nombre_carpeta)

	def crear_archivo(self):
		with open(f"{self.nombre_carpeta}/{self.nombre_archivo}", 'w') as file:
			file.write(f"Documento {self.nombre_archivo}, propiedad de {self.own}")

	def borrar_todo(self):
		if os.path.exists(self.nombre_carpeta):
			shutil.rmtree(self.nombre_carpeta)
			print(f"Se ha eliminado la carpeta {self.nombre_carpeta} con todo su contenido")

		else:
			print("No se pudo eliminar la carpeta")

# Creacion del objeto de clase SistemaOperativo
usuario1 = SistemaOperativo('contabilidad.doc', 'documentos', 'Pablo')

eleccion = input("Escribe 1 para crear carpeta y archivo o 2 para borrarlo todo: ")
if eleccion == "1":
	try:
		# Llamda a los metodos de este objeto
		usuario1.crear_carpeta()
		usuario1.crear_archivo()

	except:
		usuario1.borrar_todo()
		usuario1.crear_carpeta()
		usuario1.crear_archivo()

	finally:
		print("El programa ha finalizado")

elif eleccion == "2":
	try:
		usuario1.borrar_todo()

	except:
		print("Hubo un error al eliminar los archivos o no existen")
		