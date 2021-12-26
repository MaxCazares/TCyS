from tkinter import *
from tkinter import ttk
import tkinter as tk
from Grabadora import grabar
from Analisis import analizaAudio, getAmplitudes, startAnalisis
from Graficas import graficaEspectroFrecuencias, graficaAudio
from formantes import getFormantes
from Identificacion import identificar
from matplotlib import pyplot as plt
import librosa
from librosa import display
import threading
import time
from tkinter import PhotoImage
from PIL import Image,ImageTk
import easygui as eg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

global interfaz
global vocalEncontrada

#---------------------------------------------------------------------------------
def Grabar():
    promediosH = {}
    grabar()
    promediosH = startAnalisis()
    b1 = tk.Button(interfaz,bg='#480000', fg='#FFFFFF',cursor="hand1",text="Grafica de Audio",command=lambda: graficaAudio(analisis['muestras'], analisis['tasa_muestreo']))
    b1.place(x = 180, y = 370)
    b2 = tk.Button(interfaz,bg='#480000', fg='#FFFFFF',cursor="hand1",text="Grafica de Espectro de Frecuencia",command=lambda: graficaEspectroFrecuencias(amp, int(analisis['tasa_muestreo'])))
    b2.place(x = 135, y = 405)

    analisis = analizaAudio("data/audio.wav")
    amp = getAmplitudes(analisis['muestras'])
    formante = getFormantes("data/audio.wav")
    print("F1: ", formante[0])
    print("F2: ", formante[1])
    vocaL = str(identificar(formante, promediosH)) 
    resultado = StringVar()
    vocalEncontrada = Label(interfaz, textvariable = resultado, font=("Verdana",70), bg='#480000', fg='#FFFFFF')
    vocalEncontrada.place(x = 195, y = 200)

    resultado.set(' ')
    resultado.set(vocaL)
    print(vocaL)
# 
#---------------------------------------------------------------------------------
def iniciaContador():
    pb.start(12)
    time.sleep(1.2)
    pb.stop()

#----------------------------------------------------------------------------------
def iniciar():
    t1 = threading.Thread(name = "iniciaContador", target = iniciaContador)
    t2 = threading.Thread(name = "Grabar", target = Grabar) 
    t1.start()
    t2.start()

#INICIO----------------------------------------------------------------------------------------------------

if __name__=='__main__':
    # flag = False
    interfaz = tk.Tk()
    # Ventana
    interfaz.geometry('480x470') 
    interfaz.config(bd=10, bg='#480000')
    interfaz.title('Proyecto Final')

    info = Label(interfaz,bd = 0, text = 'Grupo: 3CV16, TCyS', font=("Verdana",12), bg='#480000', fg='#FFFFFF')
    info.place(x = 150, y = 17)
    # info.pack()

    img = Image.open('data/microfono.png')
    img = img.resize((50, 50), Image.ANTIALIAS) 
    img = ImageTk.PhotoImage(img)
    botonGrabar = tk.Button(interfaz, image=img, text="Grabar", compound="top", command=iniciar, bg='#480000', fg='#FFFFFF')
    botonGrabar.place(x = 200, y = 50)
    # botonGrabar.pack() 

    ipn = Image.open('data/ipn.png')
    ipn = ipn.resize((120, 85), Image.ANTIALIAS) 
    ipn = ImageTk.PhotoImage(ipn)
    ipnLogo = Label(interfaz, image = ipn, bg='#FFFFFF', fg='#FFFFFF')
    # ipnLogo.config(bg='systemTransparent')
    ipnLogo.place(x = 0, y = 17)

    escom = Image.open('data/escom.png')
    escom = escom.resize((85, 85), Image.ANTIALIAS) 
    escom = ImageTk.PhotoImage(escom)
    escomLogo = Label(interfaz, image = escom, bg='#FFFFFF', fg='#FFFFFF')
    # ipnLogo.config(bg='systemTransparent')
    escomLogo.place(x = 370, y = 17)

    pb = ttk.Progressbar(interfaz, orient="horizontal", length=200)
    pb.place(x = 140, y = 135)
    # pb.pack()

    label = Label(interfaz, text = 'Letra Encontrada:', font=("Verdana",12), bg='#480000', fg='#FFFFFF')
    label.place(x = 160, y = 175)
    # label.pack()

    pb.config(mode="determinate", maximum=100, value = 0)
    pb.step(100)

    interfaz.mainloop()