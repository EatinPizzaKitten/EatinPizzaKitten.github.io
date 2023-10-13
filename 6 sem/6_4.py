from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Adolf Hitler")
root.geometry("600x300")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

alp= {'0': 'f', '1': 'e', '2': 'd', '3': 'c', '4': 'b', '5': 'a', '6': '9', '7': '8', '8': '7', '9': '6', 'a': '5', 'b': '4', 'c': '3', 'd': '2', 'e': '1', 'f': '0'}
def comp_color(*args):
    hex = str(vvod.get())
    com = ''.join(alp.get(ch, ch) for ch in hex)
    try:
        if len(hex) == 6:
            ans.set('#' + com)
        else:
            ans.set('wrong number')
    except ValueError:
        pass

vvod = StringVar()
vvod_entry = ttk.Entry(mainframe, width=7, textvariable=vvod)
vvod_entry.grid(column=2, row=1, sticky=(W, E))

ans = StringVar()
ttk.Label(mainframe, textvariable=ans).grid(column=3, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Вычислить", command=comp_color).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Введите цвет в HEX   #").grid(column=1, row=1, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

vvod_entry.focus()
root.bind("<Return>", comp_color)
root.mainloop()