from modelo import obtener_pokemones, eliminar_pokemon
from tkinter import messagebox

def cargar_datos_en_grilla(grilla):
    """Obtiene los datos del modelo y los carga en la grilla."""
    pokemons = obtener_pokemones()
    for poke in pokemons:
        grilla.insert(parent='', index='end', values=poke)

def eliminar_pokemon_seleccionado(grilla):
    """Elimina el Pokémon seleccionado en la grilla."""
    try:
        select_poke = grilla.selection()[0]
        poke_values = grilla.item(select_poke, 'values')
        nombre = poke_values[1]

        eliminar_pokemon(nombre)
        grilla.delete(select_poke)
    except IndexError:
        messagebox.showwarning("Advertencia", "No has seleccionado ningún Pokémon.")