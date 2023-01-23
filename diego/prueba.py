import tkinter as tk
from tkinter import PhotoImage

ventana = tk.Tk()

ventana.title("Ventana prueba Arcane Signet")
ventana.geometry("500x500")

# Cargar la imagen
imagen = PhotoImage(file="C:\Users\dgill\OneDrive\Documentos\Personal\magic-python\diego\img\arcane-signet.png")

# Crear una etiqueta para mostrar la imagen
etiqueta_imagen = tk.Label(ventana, image=imagen)

# Configurar el tamaño de la imagen
etiqueta_imagen.config(width=150, height=100)
etiqueta_imagen.pack()

ventana.mainloop()