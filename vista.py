import tkinter as tk
from tkinter import ttk
from controlador import cargar_datos_en_grilla, eliminar_pokemon_seleccionado

#Configuración de la ventana principal
window = tk.Tk()
window.geometry("800x500")
window.title("POKÉDEX")

#Definición de la grilla
grilla = ttk.Treeview(window, height=10, columns=['#id', "Nombre", "Category"])
grilla.column("#0", width=0, stretch=tk.NO)
grilla.column("#id", width=100, minwidth=30)
grilla.column("Nombre", width=150, minwidth=30)
grilla.column("Category", width=150, minwidth=30)
grilla.heading("#id", text="id")
grilla.heading("Nombre", text="Nombre")
grilla.heading("Category", text="Categoría")
grilla.grid(row=11, column=0, padx=60, pady=10, sticky=("W""N"))

#Cargar datos en la grilla
cargar_datos_en_grilla(grilla)

#Botón para eliminar Pokémon
boton_eliminar = tk.Button(window, text="Eliminar Pokémon", command=lambda: eliminar_pokemon_seleccionado(grilla))
boton_eliminar.grid(row=1, column=0, padx=350, pady=10, sticky="W")

window.mainloop()