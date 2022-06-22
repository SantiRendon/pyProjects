#Herramientas: 
#   Tkinder (Modulo de Python para UI)
#   MySQL (Base de datos)

import this
from tkinter import ttk
from tkinter import *

import sqlite3
 # Modulo para coneccion a base de datos

class Product:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Products Application')

        #Creando un Frame Container
        frame = LabelFrame(self.wind, text = 'Register A new Product')
        frame.grid(row=0, column=0,columnspan=3,pady=20,) # < < < posicionar Frame container

        #Name Input
        Label(frame, text= 'Name: ').grid(row=1,column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)

        #Price Input
        Label(frame, text= 'Price: ').grid(row=2,column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)

        #Button Add Product
        ttk.Button(frame, text='Save Product').grid(row=3,columnspan=2,sticky=W + E)

        #Table
        self.tree=ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0,columnspan=2)
        self.tree.heading('#0', text='Name',anchor=CENTER)
        self.tree.heading('#1', text='Price',anchor=CENTER)

# comprobacion del archivo main
if __name__=='__main__':
        window=Tk()
        application = Product(window)
        window.mainloop()
