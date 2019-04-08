from tkinter import ttk
from tkinter import *

import sqlite3

class Contact:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Listado de Contactos - By Ing. Gerson Altamirano')

        #Crear un contenedor del formulario
        frame = LabelFrame(self.wind, text = 'Nombre de Contacto')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #Crear una etiqueta y un campo de input
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.nombre = Entry(frame)
        self.nombre.grid(row = 1, column = 1)

        #Crear una etiqueta y un campo de input
        Label(frame, text = 'Telefono: ').grid(row = 2, column = 0)
        self.telefono = Entry(frame)
        self.telefono.grid(row = 2, column = 1)

        #Crear una etiqueta y un campo de input
        Label(frame, text = 'Correo: ').grid(row = 3, column = 0)
        self.email = Entry(frame)
        self.email.grid(row = 3, column = 1)

if __name__ == '__main__':
    window = Tk()
    app = Contact(window)
    window.mainloop()