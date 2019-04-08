from tkinter import ttk
from tkinter import *

import sqlite3

class Contact:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Listado de Contactos - By Ing. Gerson Altamirano')

if __name__ == '__main__':
    window = Tk()
    app = Contact(window)
    window.mainloop()