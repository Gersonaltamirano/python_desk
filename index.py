from tkinter import ttk
from tkinter import *

import sqlite3

class Contact:

    db_name = 'contactos.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title('Listado de Contactos - By Ing. Gerson Altamirano')

        #Crear un contenedor del formulario
        frame = LabelFrame(self.wind, text = 'Nombre de Contacto')
        frame.grid(row = 0, column = 0, columnspan = 4, pady = 20)

        #Crear una etiqueta y un campo de input
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.nombre = Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row = 1, column = 1)

        #Crear una etiqueta y un campo de input
        Label(frame, text = 'Telefono: ').grid(row = 2, column = 0)
        self.telefono = Entry(frame)
        self.telefono.grid(row = 2, column = 1)

        #Crear una etiqueta y un campo de input
        Label(frame, text = 'Correo: ').grid(row = 3, column = 0)
        self.email = Entry(frame)
        self.email.grid(row = 3, column = 1)

        #Boton que almacenará los datos de los input
        ttk.Button(frame, text = 'Guardad contacto').grid(row = 4, columnspan = 2, sticky = W + E )

        #Agreando tabla donde se mostrarán los registros
        self.tree = ttk.Treeview(height = 15 )
        self.tree['columns']=('#1', '#2','#3')
        self.tree.grid(row = 6, column = 0, columnspan = 4)
        self.tree.heading('#0', text = 'Indice', anchor = CENTER)
        self.tree.heading('#1', text = 'Nombre', anchor = CENTER)
        self.tree.heading('#2', text = 'Telefono', anchor = CENTER)
        self.tree.heading('#3', text = 'Email', anchor = CENTER)

    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_contactos(self):

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        query = 'SELECT * FROM contactos ORDER BY nombre DESC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])

if __name__ == '__main__':
    window = Tk()
    app = Contact(window)
    window.mainloop()