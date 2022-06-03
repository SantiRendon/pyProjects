#Como crear GUI (Graphics User Interface) en python 
# documentacion de la libreria tkinter: https://docs.python.org/es/3/library/tkinter.html
# ver Interfaces gráficas I: https://www.youtube.com/watch?v=hTUJC8HsC2I
from tkinter import *

raiz=Tk() #Variable con el metodo Tk

raiz.title("Primera ventana") #cambiar nombre de la ventana

raiz.resizable(True,False) # impedir que se pueda cambiar el tamaño de la ventana # 
   #width:Ancho ||    ||Height:Alto

raiz.iconbitmap("img/Avocado.ico") #cambiar el icono de la ventana por otro archivo .ico

raiz.geometry("650x350") #establecer tamaño de la ventana al abrir WIDTHxHEIGHT

raiz.config(bg="#268251") # cambiar color de fondo de la ventana con bg

raiz.mainloop() #metodo main