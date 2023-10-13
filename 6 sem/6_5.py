from random import randint, choice
from tkinter import *
from tkinter import ttk

WIDTH = 500
HEIGHT = 500

v = [-10, 10]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'white', 'pink', 'brown']
class Ball:
    def __init__(self, *args):
        self.R = randint(10, 20) #храним размер, при каждом создании объекта будет выбираться случайно
        self.x = randint(self.R, WIDTH - self.R) # храним положение по x и y
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = (choice(v), choice(v)) # это по сути шаг движения шаров. если увеличить -- будут двигаться быстрее
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R, fill=choice(colors)) # при создании шарика отрисовываем его

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0: # отражение от стенок
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0: # отр
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def click_handler(event):
    balls.append(Ball(event.x, event.y))

#здесь мы уже привычно обращаемся к balls как к глобальной переменной. На самом деле дело в том, что нам лень писать классы.
def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
canvas = Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
canvas.bind('<Button-1>', click_handler)
balls = [Ball() for i in range(5)]
tick()
root.resizable(None, None)
root.mainloop()