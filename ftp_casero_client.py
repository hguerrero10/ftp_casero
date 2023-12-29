import socket
import tkinter as tk
from tkinter import filedialog

def send_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("All files", "*.*"),))
    if filename:
        client_socket.send(bytes(filename, "utf-8"))

root = tk.Tk()
root.title("Transferencia de Archivos")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.12.44', 12345))  # Reemplaza 'IP_del_servidor' por la IP de tu laptop

file_button = tk.Button(root, text="Enviar archivo", command=send_file)
file_button.pack()

root.mainloop()
