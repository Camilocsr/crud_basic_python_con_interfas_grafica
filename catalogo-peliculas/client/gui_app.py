import tkinter as tk
from tkinter import ttk #Importante sin esto no se pueden hacer tablas...
from model.pelicula_dao import crear_tabla, borrar_tabla

def barra_menu(root):
    barra_menu = tk.Menu(root) #se crea la barra de menu principal...
    root.config(menu = barra_menu, width = 300, height = 300) #se configura las medidas de la barra de menu...

    menu_inicio = tk.Menu(barra_menu, tearoff=0) #Se crea la primera sub obcion del la bbarra de menu
    barra_menu.add_cascade(label='Inicio', menu = menu_inicio) #se agrega.

    menu_inicio.add_command(label='crear reguistro', command=crear_tabla) #Se agrega...
    menu_inicio.add_command(label='eliminar reguistro', command=borrar_tabla) #Borra la base de datos...
    menu_inicio.add_command(label='Salir del programa.', command=root.destroy)#cierra el programa por completo...

    # barra_menu.add_cascade(label='hola')

class Frame(tk.Frame): #classe de el contenedor
    def __init__(self, root = None): #constructor principal, el que se ejucutara de primeras apenas se ejecute dicho programa
        super().__init__(root,width= 480, height= 320) #iteracion de el objeto principal..
        self.root = root
        self.pack() #enpaquetamiento
        self.config(bg= 'darkmagenta') #configuracion del contenedor..

        self.campos_pelicula()
        self.desabilitar_campos()
        self.tabla_peliculas()

    def campos_pelicula(self): #metodo para el ingreso de datos por medio de los inputs..
        #Los labels son los titulos que indican que dato debe ingresar en los inputs...
        self.label_nombre = tk.Label(self, text='Nombre')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0,column=0,padx=10,pady=10)

        self.label_duracion = tk.Label(self, text='Duracion')
        self.label_duracion.config(font=('Arial', 12, 'bold'))
        self.label_duracion.grid(row=1,column=0,padx=10,pady=10)

        self.label_genero = tk.Label(self, text='Genero')
        self.label_genero.config(font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=2,column=0,padx=10,pady=10)

        self.mi_nombre = tk.StringVar()
        #Los entry son los input donde la persona que utiliza el programa ingresa los datos correspondientes que sele indicaron gracias a los labels..
        self.entry_nombre = tk.Entry(self, textvariable= self.mi_nombre)
        self.entry_nombre.config(width=50,font=('Arial', 12, 'bold'))
        self.entry_nombre.grid(row=0,column=1,padx=10,pady=10, columnspan=2)

        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable=self.mi_genero)
        self.entry_genero.config(width=50,font=('Arial', 12, 'bold'))
        self.entry_genero.grid(row=1,column=1,padx=10,pady=10, columnspan=2)

        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.mi_duracion)
        self.entry_duracion.config(width=50,font=('Arial', 12, 'bold'))
        self.entry_duracion.grid(row=2,column=1,padx=10,pady=10, columnspan=2)

        #Botones que indican los funcionamientos a relizar segun la eleccion de la persona...
        self.btn_Nuevo = tk.Button(self, text='Nuevo',command= self.habilitar_campos)
        self.btn_Nuevo.config(width= 10, font=('Arial', 12, 'bold'), fg='darkmagenta',bg='darkblue', cursor='hand2', activebackground= 'green')
        self.btn_Nuevo.grid(row=3, column=0,padx=10,pady=10)

        self.btn_guardar = tk.Button(self, text='Guardar', command=self.guaradar_datos)
        self.btn_guardar.config(width= 10, font=('Arial', 12, 'bold'), fg='darkmagenta',bg='darkblue', cursor='hand2', activebackground= 'green')
        self.btn_guardar.grid(row=3, column=1,padx=10,pady=10)

        self.btn_cancelar = tk.Button(self, text='Cancelar.', command= self.desabilitar_campos)
        self.btn_cancelar.config(width= 10, font=('Arial', 12, 'bold'), fg='darkmagenta', bg='darkblue', cursor='hand2', activebackground= 'green')
        self.btn_cancelar.grid(row=3, column=2,padx=10,pady=10)

    #metodo para desabilitar campos de entrada de datos y botones...

    #Metodo para habilitar los campos cuando se seleccione el boton nuevo...
    def habilitar_campos(self):
        #Se habilitan los campos de entrada de datos...
        self.entry_nombre.config(state= 'normal')
        self.entry_duracion.config(state= 'normal')
        self.entry_genero.config(state= 'normal')

        #Se habilitan los botones...
        self.btn_guardar.config(state= 'normal')
        self.btn_cancelar.config(state= 'normal')

    #Metodo el cual se encarga de enviar los datos y guardarlos en la tabla y en la base de datos...
    def guaradar_datos(self):
        self.desabilitar_campos()

    #Metodo el cual se encarga de desahabilitar los campos si todavia no se a seleccionado el boton nuevo o si se selecciona el boton cancelar...
    def desabilitar_campos(self):
        #se envia al input datos bacios...
        self.mi_nombre.set('')
        self.mi_genero.set('')
        self.mi_duracion.set('')

        #se desabilita cada uno de los campos...
        self.entry_nombre.config(state= 'disabled')
        self.entry_duracion.config(state= 'disabled')
        self.entry_genero.config(state= 'disabled')

        #se desablita los botones...
        self.btn_guardar.config(state= 'disabled')
        self.btn_cancelar.config(state= 'disabled')

    #Metodo que se encarga de la creacion de la tabla la cual se vera al ejecutar el programa...
    def tabla_peliculas(self):
        self.tabla = ttk.Treeview(self, columns=('Nombre', 'duracion', 'genero'))
        self.tabla.grid(row=4,columnspan=4)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Duración')
        self.tabla.heading('#3', text='Genero')

        self.tabla.insert('',0, text='1', values=(self.entry_nombre, self.entry_duracion, self.entry_genero))

        self.btn_eliminar = tk.Button(self, text='Eliminar')
        self.btn_eliminar.config(width= 10, font=('Arial', 12, 'bold'), fg='darkmagenta',bg='darkblue', cursor='hand2', activebackground= 'green')
        self.btn_eliminar.grid(row=5, column=0,padx=10,pady=10)

        self.btn_editar = tk.Button(self, text='Editar.')
        self.btn_editar.config(width= 10, font=('Arial', 12, 'bold'), fg='darkmagenta', bg='darkblue', cursor='hand2', activebackground= 'green')
        self.btn_editar.grid(row=5, column=2,padx=10,pady=10)