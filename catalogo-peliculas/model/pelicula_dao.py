from .conexion_db_ import conexionDb

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

    conexion.cursor.execute(sql)
    conexion.cerrar()

def borrar_tabla():
    conexion = conexionDb()

    sql = 'DROP TABLE peliculas'
    conexion.cursor.execute(sql)
    conexion.cerrar()