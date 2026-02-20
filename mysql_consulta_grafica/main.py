import customtkinter as ctk
from database import TipoConsulta
import database
from tkinter import messagebox

def limpiar_pantalla():
    # Oculta todos los widgets de la interfaz
    for widget in todos_los_widgets:
        widget.pack_forget()
    etiqueta_clic.configure(text="")

def mostrar_pantalla(lista_widgets):
    # Limpia primero y luego muestra solo los widgets de la lista pasada
    limpiar_pantalla()
    for widget in lista_widgets:
        widget.pack(pady=10)

def mostrar_crear():
    mostrar_pantalla(widgets_crear)

def mostrar_consultar():
    mostrar_pantalla(widgets_consultar)

def click_inicio():
    mostrar_pantalla(widgets_inicio)

def click_crear():
    print("Intentando crear usuario...")
    nombre = entry_name.get().strip()
    email = entry_email.get().strip()
    exito, mensaje = database.insertar_usuario(nombre, email)

    if exito:
        messagebox.showinfo("Éxito", mensaje)
        entry_name.delete(0, 'end')
        entry_email.delete(0, 'end')

    else:
        messagebox.showerror("Error", mensaje)

def click_consultar(tipo: TipoConsulta):
    resultados = database.consultar_datos(tipo)
    etiqueta_clic.configure(text="\n".join(resultados))

ventana = ctk.CTk()
ventana.title("Conexión a MySQL")
ventana.geometry("400x400")

label = ctk.CTkLabel(ventana, text="Conexión a MySQL con Python", font=("Arial", 16))
label.pack(pady=20)

etiqueta_clic = ctk.CTkLabel(ventana, text="")

entry_name = ctk.CTkEntry(ventana, width=300)
entry_email = ctk.CTkEntry(ventana, width=300)

# El lambda es necesario para pasar argumentos a la función sin ejecutarla inmediatamente
button_aparecer_crear = ctk.CTkButton(ventana, text="Crear usuario y email", command = lambda: mostrar_crear())
button_aparecer_crear.pack(pady=10)

button_aparecer_consultar = ctk.CTkButton(ventana, text="Consultar Base de Datos", command = lambda: mostrar_consultar())
button_aparecer_consultar.pack(pady=10)

button_inicio = ctk.CTkButton(ventana, text="Ir al inicio", command = lambda: click_inicio())

button_nombres = ctk.CTkButton(ventana, text="Consultar Nombres", command = lambda: click_consultar(TipoConsulta.NOMBRES))
button_emails = ctk.CTkButton(ventana, text="Consultar emails", command = lambda: click_consultar(TipoConsulta.EMAILS))
button_consultar_db = ctk.CTkButton(ventana, text="Consultar toda la base de Datos", command = lambda: click_consultar(TipoConsulta.TODO))

button_crear = ctk.CTkButton(ventana, text="Añadir usuario, email", command = lambda: click_crear())

etiqueta_clic.pack(pady=10)

widgets_inicio = [button_aparecer_crear, button_aparecer_consultar]
widgets_crear = [entry_name, entry_email, button_crear, button_inicio]
widgets_consultar = [button_nombres, button_emails, button_consultar_db, button_inicio]

# Una lista maestra con todo para limpiar la pantalla rápido
todos_los_widgets = [
    button_aparecer_crear, button_aparecer_consultar, 
    entry_name, entry_email, button_crear, 
    button_nombres, button_emails, button_consultar_db, button_inicio
]

ventana.mainloop()

