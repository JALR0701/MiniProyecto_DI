import tkinter as tk #Se importan las librerias a usar
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

Main.geometry('%dx%d+%d+%d' % (w, h, x, y))
Main.resizable(0,0)
Main. config (background = "Black")

com = tk.Label(Main, text = "COM:" + numero, bg = "black", fg = "white", font = ("Times New Roman", 24)) #Label que muestra el COM utilizado
com.pack()
