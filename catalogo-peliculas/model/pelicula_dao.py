from .conexion_db_ import conexionDb
from tkinter import messagebox

def crear_tabla():
    conexion = conexionDb()

    sql = '''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        tittle = 'Crear registro'
        mesaje = 'Se creo la tabla en la base de datos.'
        messagebox.showinfo(tittle, mesaje)
    except:
        tittle = 'Crear registro'
        mesaje = 'Error al crear la base de datos ya que, existe una.'
        messagebox.showerror(tittle, mesaje)

def borrar_tabla():
    conexion = conexionDb()

    sql_borrar = 'DROP TABLE peliculas'

    try:
        conexion.cursor.execute(sql_borrar)
        conexion.cerrar()
        tittle = 'borrar registro registro'
        mesaje = 'Se borro la base de datos sactisfactoriamente.'
        messagebox.showinfo(tittle, mesaje)
    except:
        tittle = 'Borrar registro'
        mesaje = 'Error al Borrar la base de datos ya que no existe una.'
        messagebox.showerror(tittle, mesaje)