import tkinter as tk

# Diccionario de palabras y sus significados
diccionario = {
    "perro": "Un mamífero domesticado comúnmente utilizado como mascota.",
    "gato": "Un felino doméstico con pelaje suave y hábitos independientes.",
    "ordenador": "Una máquina electrónica que procesa datos y realiza cálculos."
    # Puedes agregar más palabras y significados según sea necesario
}

def buscar_palabra():
    palabra = palabra_entry.get().lower()
    if palabra in diccionario:
        significado_label.config(text=f"Significado de '{palabra}': {diccionario[palabra]}")
    else:
        significado_label.config(text=f"'{palabra}' no está en el diccionario.")

root = tk.Tk()
root.title("Diccionario")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

palabra_label = tk.Label(frame, text="Ingresa una palabra:")
palabra_label.pack()

palabra_entry = tk.Entry(frame)
palabra_entry.pack()

buscar_button = tk.Button(frame, text="Buscar", command=buscar_palabra)
buscar_button.pack()

significado_label = tk.Label(frame, text="")
significado_label.pack()

root.mainloop()
