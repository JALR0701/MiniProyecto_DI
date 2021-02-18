import tkinter as tk #Se importan las librerias a usar
from PIL import ImageTk, Image
import serial
import struct
import time

while(1): #Se inicializa la conexion con el puerto
    while(1):
        try:
            numero = str(int(input(">  COM: ")))
            port = "com" + numero
            break
        except:
            print ("Enter a numeric value")
    try:
        data = serial.Serial(port, baudrate = 9600, timeout=1500)
        break
    except:
        print("Unable to open port")

Main = tk.Tk() #Se crea la vetana principal y sus caracteristicas
Main.title("Comunicación serial")
w = 1080 
h = 720

ws = Main.winfo_screenwidth()
hs = Main.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

Main.geometry("{0}x{1}+0+0".format(Main.winfo_screenwidth(), Main.winfo_screenheight()))
Main.resizable(0,0)
Main. config (background = "Black")

com = tk.Label(Main, text = "COM:" + numero, bg = "black", fg = "white", font = ("Times New Roman", 24)) #Label que muestra el COM utilizado
com.pack()

Brazo = Image.open("Brazo.png")
Brazo=Brazo.resize((300,200))
Brazo = ImageTk.PhotoImage(Brazo)
label = tk.Label(Main, image=Brazo, bg="black")
label.pack()

Base = Image.open("Base.png")
Base=Base.resize((200,200))
Base = ImageTk.PhotoImage(Base)
label = tk.Label(Main, image=Base, bg="black")
label.place(x = 75, y = 300)

Eslabon1 = Image.open("Eslabon1.png")
Eslabon1=Eslabon1.resize((300,200))
Eslabon1 = ImageTk.PhotoImage(Eslabon1)
label = tk.Label(Main, image=Eslabon1, bg="black")
label.place(x = 350, y = 300)

Eslabon2 = Image.open("Eslabon2.png")
Eslabon2 = Eslabon2.resize((300,200))
Eslabon2 = ImageTk.PhotoImage(Eslabon2)
label = tk.Label(Main, image=Eslabon2, bg="black")
label.place(x = 700, y = 300)
