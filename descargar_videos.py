import tkinter as tk
from pytube import YouTube

def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
        status_label.config(text="¡Descarga completa!")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

root = tk.Tk()
root.title("Descargar Video de YouTube")

url_label = tk.Label(root, text="URL del video:")
url_label.pack()

url_entry = tk.Entry(root, width=40)
url_entry.pack()

download_button = tk.Button(root, text="Descargar", command=download_video)
download_button.pack()

status_label = tk.Label(root, text="", fg="red")
status_label.pack()

root.mainloop()
