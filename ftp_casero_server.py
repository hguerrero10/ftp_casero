import socket
import tkinter as tk
from tkinter import filedialog

def send_file():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",  filetypes=(("All files", "*.*"),))
    if filename: client_socket.send(bytes(filename, "utf-8"))

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.207.28', 12345))  # Puedes cambiar el puerto si es necesario
    server_socket.listen(1)
    status_label.config(text="Esperando conexión con el servicio...")
    global client_socket
    client_socket, addr = server_socket.accept()
    status_label.config(text=f"Conectado: {addr}")
    file_button.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Transferencia de Archivos")

status_label = tk.Label(root, text="Esperando conexión...", padx=10, pady=10)
status_label.pack()

start_button = tk.Button(root, text="Iniciar servidor", command=start_server)
start_button.pack()

file_button = tk.Button(root, text="Enviar archivo", command=send_file, state=tk.DISABLED)
file_button.pack()

root.mainloop()
