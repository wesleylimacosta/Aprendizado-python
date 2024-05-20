import webbrowser
from tkinter import *

root = Tk()
root.title("Open Browser")
root.geometry("300x200")

url = "https://www.youtube.com/watch?v=__h2D0XDZlY"

def open_browser():
    # Use o comando específico para abrir no navegador padrão do Windows
    webbrowser.get('windows-default').open(url)

myyoutube = Button(root, text="Abrir vídeo do YouTube", command=open_browser)
myyoutube.pack(pady=20)

root.mainloop()
