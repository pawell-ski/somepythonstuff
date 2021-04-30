from tkinter import *
from tkinter import filedialog
import os, sys
import tkinter as tk
from PIL import Image, ImageTk, ImageOps #what

def openfile():
    filepath = filedialog.askopenfilename(title = "open image", filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All files","*.*")))
    file = open(filepath,'r')
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img
    


def showimage():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title = "open image", filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All files","*.*")))
    img = Image.open(fln)
    img.thumbnail((350,350))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img


def gray():
    img = ImageTk.PhotoImage(img)
    image = ImageOps.grayscale(img)

    


root = Tk()


frm = Frame(root)
frm.pack(side=BOTTOM, padx =15, pady= 15)

lbl = Label(root)
lbl.pack()

btn = Button(frm, text = "Abrir Imagem", command = showimage)
btn.pack(side=tk.TOP)

btn2 = Button(frm, text = "GRAY", command = gray)
btn2.pack(side=tk.RIGHT)


root.title("Ibagens :^)")
root.geometry("300x350")
root.mainloop()
