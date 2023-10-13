from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Adolf Hitler")
root.geometry("300x300")

def calculate(*args):
    try:
        value = str(vvod.get())
        otvet.set(eval(value))
    except ValueError:
        pass

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


vvod = StringVar()
vvod_entry = ttk.Entry(mainframe, width=7, textvariable=vvod)
vvod_entry.grid(column=2, row=1, sticky=(W, E))

otvet = StringVar()
ttk.Label(mainframe, textvariable=otvet).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Решить", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Введите выражение").grid(column=3, row=1, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

vvod_entry.focus()
root.bind("<Return>", calculate)
root.mainloop()