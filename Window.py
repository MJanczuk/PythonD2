import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image

Konstruktor = tkinter.Tk()
Konstruktor.attributes('-fullscreen',True)
def End():
    Konstruktor.quit()
TekstGlowny = tkinter.Label(Konstruktor, text="Hello, World").grid(row=0, column=0)
EndButt = tkinter.Button(text="Quit",command=End).grid(row=0, column=1)
Konstruktor.mainloop()