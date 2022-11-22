import tkinter as tk

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu = menu_inicio)

    menu_inicio.add_command(label='cerar reguistro')
    menu_inicio.add_command(label='eliminar reguistro')
    menu_inicio.add_command(label='Salir del programa.', command=root.destroy)

    barra_menu.add_cascade(label='hola')

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width= 480, height= 320)
        self.root = root
        self.pack()
        self.config(bg= 'darkmagenta')

        self.campos_pelicula()
        self.desabilitar_campos()

    def campos_pelicula(self):
        self.label_nombre = tk.Label(self, text='Nombre')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0,column=0,padx=10,pady=10)

        self.label_duracion = tk.Label(self, text='Duracion')
        self.label_duracion.config(font=('Arial', 12, 'bold'))
        self.label_duracion.grid(row=1,column=0,padx=10,pady=10)

        self.label_genero = tk.Label(self, text='Genero')
        self.label_genero.config(font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=2,column=0,padx=10,pady=10)

        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.config(width=50,font=('Arial', 12, 'bold'))
        self.entry_nombre.grid(row=0,column=1,padx=10,pady=10, columnspan=2)

        self.entry_genero = tk.Entry(self)
        self.entry_genero.config(width=50,font=('Arial', 12, 'bold'))
        self.entry_genero.grid(row=1,column=1,padx=10,pady=10, columnspan=2)

        self.entry_duracion = tk.Entry(self)
        self.entry_duracion.config(width=50,font=('Arial', 12, 'bold'))
        self.entry_duracion.grid(row=2,column=1,padx=10,pady=10, columnspan=2)

        #botones...
        self.btn_Nuevo = tk.Button(self, text='Nuevo',command= self.habilitar_campos)
        self.btn_Nuevo.config(width= 10, font=('Arial', 12, 'bold'), fg='darkmagenta',bg='darkblue', cursor='hand2', activebackground= 'green')
        self.btn_Nuevo.grid(row=4, column=0,padx=10,pady=10)

        self.btn_guardar = tk.Button(self, text='Guardar')
        self.btn_guardar.config(width= 10, font=('Arial', 12, 'bold'), fg='darkmagenta',bg='darkblue', cursor='hand2', activebackground= 'green')
        self.btn_guardar.grid(row=4, column=1,padx=10,pady=10)

        self.btn_cancelar = tk.Button(self, text='Cancelar.')
        self.btn_cancelar.config(width= 10, font=('Arial', 12, 'bold'), fg='darkmagenta', bg='darkblue', cursor='hand2', activebackground= 'green')
        self.btn_cancelar.grid(row=4, column=2,padx=10,pady=10)

    #metodo para desabilitar campos de entrada de datos y botones...

    def habilitar_campos(self):
        self.entry_nombre.config(state= 'normal')
        self.entry_duracion.config(state= 'normal')
        self.entry_genero.config(state= 'normal')

        self.btn_guardar.config(state= 'normal')
        self.btn_cancelar.config(state= 'normal')

    def desabilitar_campos(self):
        self.entry_nombre.config(state= 'disabled')
        self.entry_duracion.config(state= 'disabled')
        self.entry_genero.config(state= 'disabled')

        self.btn_guardar.config(state= 'disabled')
        self.btn_cancelar.config(state= 'disabled')