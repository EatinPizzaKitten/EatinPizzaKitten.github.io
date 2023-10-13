from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Adolf Hitler")
root.geometry("600x300")

def BMI(*args):
    try:
        h = float(height.get()) * 0.01
        w = float(weight.get())
        bim = w / (h*h)
        otvet.set(round(w/(h*h), 3))
        if bim < 25:
            mean.set('У вас нормальный вес')
        elif 25 <= bim < 30:
            mean.set('У вас лишний вес')
        else:
            mean.set('У вас жирная жопа')
    except ValueError:
        pass

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

height = StringVar()
height_entry = ttk.Entry(mainframe, width=7, textvariable=height)
height_entry.grid(column=2, row=1, sticky=(W, E))

weight = StringVar()
weight_entry = ttk.Entry(mainframe, width=7, textvariable=weight)
weight_entry.grid(column=3, row=1, sticky=(W, E))

otvet = StringVar()
ttk.Label(mainframe, textvariable=otvet).grid(column=2, row=2, sticky=(W, E))
mean = StringVar()
ttk.Label(mainframe, textvariable=mean).grid(column=3, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Определить", command=BMI).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Введите рост (см) и вес (кг)").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Ваш Индекс Массы Тела:").grid(column=1, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

height_entry.focus()
root.bind("<Return>", BMI)
root.mainloop()