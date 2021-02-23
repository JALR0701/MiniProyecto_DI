import tkinter as tk #Se importan las librerias a usar
from tkinter import ttk
from PIL import ImageTk, Image
from threading import Thread
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
Main. config (background = "Black")

com = tk.Label(Main, text = "COM:" + numero, bg = "black", fg = "white", font = ("Times New Roman", 24)) #Label que muestra el COM utilizado
com.pack()

data.write(struct.pack('>B',0))
presionado = True

def parar (e):
    global presionado
    presionado = False

def girarDCDer ():
    global presionado
    presionado = True
    while (presionado):
        data.write(struct.pack('>B',1))

def girarDCIzq ():
    global presionado
    presionado = True
    while (presionado):
        data.write(struct.pack('>B',2))

def girarStepDer ():
    global presionado
    presionado = True
    while (presionado):
        data.write(struct.pack('>B',3))

def girarStepIzq ():
    global presionado
    presionado = True
    while (presionado):
        data.write(struct.pack('>B',4))

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

Eslabon3 = Image.open("Eslabon3.png")
Eslabon3 = Eslabon3.resize((300,200))
Eslabon3 = ImageTk.PhotoImage(Eslabon3)
label = tk.Label(Main, image=Eslabon3, bg="black")
label.place(x = 1100, y = 300)

Eslabon4 = Image.open("Eslabon4.png")
Eslabon4 = Eslabon4.resize((300,200))
Eslabon4 = ImageTk.PhotoImage(Eslabon4)
label = tk.Label(Main, image=Eslabon4, bg="black")
label.place(x = 1500, y = 300)

Garra = Image.open("Garra.png")
Garra = Garra.resize((500,200))
Garra = ImageTk.PhotoImage(Garra)
label = tk.Label(Main, image=Garra, bg="black")
label.place(x = 500, y = 775)

giroIzq = Image.open("GiroIzq.png")
giroDer = giroIzq.transpose(Image.FLIP_LEFT_RIGHT)
giroIzq = giroIzq.resize((75,75))
giroIzq = ImageTk.PhotoImage(giroIzq)
giroDer = giroDer.resize((75,75))
giroDer = ImageTk.PhotoImage(giroDer)

arriba = Image.open("Arriba.png")
abajo = arriba.transpose(Image.FLIP_TOP_BOTTOM)
arriba = arriba.resize((75,75))
arriba = ImageTk.PhotoImage(arriba)
abajo = abajo.resize((75,75))
abajo = ImageTk.PhotoImage(abajo)

abrir = Image.open("Abrir.png")
abrir = abrir.resize((150,50))
abrir = ImageTk.PhotoImage(abrir)
cerrar = Image.open("Cerrar.png")
cerrar = cerrar.resize((150,50))
cerrar = ImageTk.PhotoImage(cerrar)

izqBase = tk.Button(Main, image = giroIzq)
izqBase.place(x = 100, y = 550)
izqBase.bind('<Button-1>',lambda e: Thread(target=girarStepIzq, daemon=True).start())
izqBase.bind('<ButtonRelease-1>',parar)

derBase = tk.Button(Main, image = giroDer)
derBase.place(x = 100, y = 650)
derBase.bind('<Button-1>',lambda e: Thread(target=girarStepDer, daemon=True).start())
derBase.bind('<ButtonRelease-1>',parar)

arribaE1 = tk.Button(Main, image = arriba)
arribaE1.place(x = 400, y = 550)

abajoE1 = tk.Button(Main, image = abajo)
abajoE1.place(x = 400, y = 650)

arribaE2 = tk.Button(Main, image = arriba)
arribaE2.place(x = 875, y = 550)

abajoE2 = tk.Button(Main, image = abajo)
abajoE2.place(x = 875, y = 650)

izqGarra = tk.Button(Main, image = giroIzq)
izqGarra.place(x = 1300, y = 550)
izqGarra.bind('<Button-1>',lambda e: Thread(target=girarDCIzq, daemon=True).start())
izqGarra.bind('<ButtonRelease-1>',parar)

derGarra = tk.Button(Main, image = giroDer)
derGarra.place(x = 1300, y = 650)
derGarra.bind('<Button-1>',lambda e: Thread(target=girarDCDer, daemon=True).start())
derGarra.bind('<ButtonRelease-1>',parar)

arribaGarra = tk.Button(Main, image = arriba)
arribaGarra.place(x = 1650, y = 550)

abajoGarra = tk.Button(Main, image = abajo)
abajoGarra.place(x = 1650, y = 650)

abrirGarra = tk.Button(Main, image = abrir)
abrirGarra.place(x = 1075, y = 825)

cerrarGarra = tk.Button(Main, image = cerrar)
cerrarGarra.place(x = 1075, y = 925)

Main.mainloop()
