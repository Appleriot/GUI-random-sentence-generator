import random
import tkinter as tk

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

names = ['Athena', 'Odysseus', 'Zeus', 'Penelope', 'Telemachus', 'Calypso', 'Circe', 'Poseidon', 'Antinous',
        'Eurymachus', 'Amphinomus', 'Eumaeus', 'Eurycleia', 'Melanthius', 'Melantho', 'Polyphemus', 'Laertes',
        'Tiresias', 'Nestor', 'Menelaus', 'Agamemnon', 'Nausicaa']
verbs = ['murder', 'genocide', 'love', 'hate', 'steal', 'bleed', 'burrow', 'waits on', 'see', 'ate', 'wants',
        'have', 'was a', 'needs', 'holds', 'pulls', 'beats', 'abuse']
words = ['pigs', 'suitors', 'bread crust', 'hens', 'humans', 'money', 'white', 'red', 'bronze', 'swords',
        'spears', 'feet', 'ankels', 'toes', 'drugs', 'buffons', 'turles', 'horeses']

window = tk.Tk()
window.geometry('600x500')
window.title("Creative respone")
window.config(padx=10, pady=10)


f = Frame(window)

xscrollbar = Scrollbar(f, orient=HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=N+S+E+W)

yscrollbar = Scrollbar(f)
yscrollbar.grid(row=0, column=1, sticky=N+S+E+W)

text = Text(f, wrap=NONE,
            xscrollcommand=xscrollbar.set,
            yscrollcommand=yscrollbar.set)
text.grid(row=0, column=0)

xscrollbar.config(command=text.xview)
yscrollbar.config(command=text.yview)

title_label = tk.Label(window, text="Random Sentences")
title_label.config(font=("Lobster", 34), fg='blue')
title_label.pack(padx=10, pady=10)

old_label_names = tk.Label(window, text=f'{random.choice(names)} {random.choice(verbs)} {random.choice(words)}.',
                            wraplength=1200, justify="left", fg='blue')
old_label_names.config(font=('Arial', 11))
old_label_names.pack(pady=10, padx=10)

def reset():
    label_names = tk.Label(window, text=f'{random.choice(names)} {random.choice(verbs)} {random.choice(words)}.',
                        wraplength=1200, justify="center").place(x=500, y=110)
    old_label_names.destroy()

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo, cursor="target")
    label.image = photo #avoid garbage collection

reset = Button(text="New Sentence", command=reset)
reset.pack()

image = Image.open('ob.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(window, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

window.mainloop()
