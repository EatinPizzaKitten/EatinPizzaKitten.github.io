import pandas as pd
from tkinter import *
from tkinter import ttk
from random import randint
films = pd.read_csv('imdb_top_250.csv')

film_genres_list = list(films['Genre'])
complex_genres = []
for film_genre in film_genres_list:
    genres = film_genre.split(' | ')
    if len(genres) > 1:
        for genre in genres:
            film_genres_list.append(genre)
        complex_genres.append(film_genre)

for genre in complex_genres:
    film_genres_list.remove(genre)

genres_set = set(film_genres_list)

root = Tk()
root.title("Adolf Hitler")
root.geometry("600x300")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

def kino(*args):
    try:
        x = str(vvod.get())
        x = x[0].upper() + x[1:].lower()
        if x in genres_set:
            while True:
                num = randint(0, len(films) - 1)
                if x in films['Genre'][num]:
                    ans.set(films['Title'][num])
                    break
                else:
                    continue
        else:
            ans.set('NO')
    except ValueError:
        pass
#print(films['Genre'][2])

vvod = StringVar()
vvod_entry = ttk.Entry(mainframe, width=7, textvariable=vvod)
vvod_entry.grid(column=2, row=1, sticky=(W, E))

ans = StringVar()
ttk.Label(mainframe, textvariable=ans).grid(column=3, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Найти нужное", command=kino).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Введите жанр").grid(column=1, row=1, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

vvod_entry.focus()
root.bind("<Return>", kino)
root.mainloop()