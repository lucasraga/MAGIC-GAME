import tkinter as tk
from tkinter import *
import os
from PIL import ImageTk,Image, ImageColor, ImageDraw

ventana = tk.Tk()
carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "img")

ventana.title("Ventana prueba Arcane Signet")

width= ventana.winfo_screenwidth() 
height= ventana.winfo_screenheight() -100             
ventana.geometry("%dx%d" % (width, height))
iconopath = os.path.join(carpeta_imagenes, "magic-icono.ico")
ventana.iconbitmap(os.path.join(carpeta_imagenes, "magic-icono.ico"))

arcanesignet = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "arcane-signet.png")).resize((84,117)))
arcanesignet_sobre = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "arcane-signet.png")).resize((168,234)))

astralcornucopia = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "astral-cornucopia.png")).resize((84,117)))
astralcornucopia_sobre = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "astral-cornucopia.png")).resize((168,234)))

contagionclasp = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "contagion-clasp.png")).resize((84,117)))
contagionclasp_sobre = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "contagion-clasp.png")).resize((168,234)))

contagionengine = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "contagion-engine.png")).resize((84,117)))
contagionengine_sobre = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "contagion-engine.png")).resize((168,234)))


everflowingchalice = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "everflowing-chalice.png")).resize((84,117)))
everflowingchalice_sobre = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "everflowing-chalice.png")).resize((168,234)))

fellwarstone = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "fellwar-stone.png")).resize((84,117)))
fellwarstone_sobre = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "fellwar-stone.png")).resize((168,234)))

carta1 = Label(image=arcanesignet)
carta2 = Label(image=astralcornucopia)
carta3 = Label(image=contagionclasp)
carta4 = Label(image=contagionengine)
carta5 = Label(image=everflowingchalice)
carta6 = Label(image=fellwarstone)

def sobre_arcane_signet(e):
    carta1.config(image=arcanesignet_sobre)
def fuera_arcane_signet(e):
    carta1.config(image=arcanesignet)
def sobre_astral_cornucopia(e):
    carta2.config(image=astralcornucopia_sobre)  
def fuera_astral_cornucopia(e):
    carta2.config(image=astralcornucopia)
def sobre_contagion_clasp(e):
    carta3.config(image=contagionclasp_sobre)
def fuera_contagion_clasp(e):
    carta3.config(image=contagionclasp)
def sobre_contagion_engine(e):
    carta4.config(image=contagionengine_sobre)
def fuera_contagion_engine(e):
    carta4.config(image=contagionengine)
    
    
def sobre_everflowing_chalice(e):
    carta5.config(image=everflowingchalice_sobre)
def fuera_everflowing_chalice(e):
    carta5.config(image=everflowingchalice)
def sobre_fellwar_stone(e):
    carta6.config(image=fellwarstone_sobre)
def fuera_fellwar_stone(e):
    carta6.config(image=fellwarstone)
    
carta1.bind("<Enter>", sobre_arcane_signet)
carta1.bind("<Leave>", fuera_arcane_signet)

carta2.bind("<Enter>", sobre_astral_cornucopia)
carta2.bind("<Leave>", fuera_astral_cornucopia)

carta3.bind("<Enter>", sobre_contagion_clasp)
carta3.bind("<Leave>", fuera_contagion_clasp)

carta4.bind("<Enter>", sobre_contagion_engine)
carta4.bind("<Leave>", fuera_contagion_engine)

carta5.bind("<Enter>", sobre_everflowing_chalice)
carta5.bind("<Leave>", fuera_everflowing_chalice)

carta6.bind("<Enter>", sobre_fellwar_stone)
carta6.bind("<Leave>", fuera_fellwar_stone)


carta1.grid(row=1, column=0, pady=10)
carta2.grid(row=1, column=1, pady=10)
carta3.grid(row=1, column=2, pady=10)
carta4.grid(row=2, column=0, pady=10)
carta5.grid(row=2, column=1, pady=10)
carta6.grid(row=2, column=2, pady=10)


ventana.mainloop()