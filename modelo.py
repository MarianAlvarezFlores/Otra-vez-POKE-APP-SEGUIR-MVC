import sqlite3

#Conexión a la base de datos

conexion = sqlite3.connect('pokedex_prueba.db')
cursor = conexion.cursor()

#Funciones del modelo

def obtener_pokemones():
    cursor.execute("SELECT * FROM pokemon")
    return cursor.fetchall()

def eliminar_pokemon(nombre):
    cursor.execute("DELETE FROM pokemon WHERE nombre = ?", (nombre,))
    conexion.commit()