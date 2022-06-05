#Algunas opciones de .config en el diseño de frames y del diseño de raiz 
# documentacion de la libreria tkinter: https://docs.python.org/es/3/library/tkinter.html
# ver Interfaces gráficas II: https://www.youtube.com/watch?v=M80CzDC1Crc

from tkinter import *

raiz=Tk() #Variable con el metodo Tk

raiz.title("segunda ventana") #cambiar nombre de la ventana

raiz.resizable(True,True) # impedir que se pueda cambiar el tamaño de la ventana # 
   #width:Ancho ||    ||Height:Alto

raiz.config(bg="#268251") # cambiar color de fondo de la ventana con bg

# Creacion del Frame #
miFrame=Frame() 
miFrame.pack(side="right",anchor="s") #empaquetar Frame con parametros de posision con SIDE y ANCHOR que funciona con los puntos cardinales en ingles
    # miFrame.pack(fill="y",expand="True") #empaquetar Frame con parametros de rellenado FILL y EXPAND
miFrame.config(bg="red") #configuracion Frame creado
miFrame.config(relief="groove",bd="20") # poner bordes a los frame con RELIEF y tamaño de borde con BD
miFrame.config(cursor="hand2") #cambiar tipo de cursor al pasarlo sobre un framse especifico
miFrame.config(width="650",height="350")

raiz.mainloop() #metodo main