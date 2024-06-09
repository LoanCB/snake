import random
import tkinter as tk

WIDTH = 10
HEIGHT = 10
CELL_SIZE = 50
SPEED = 200
DEFAULT_BODY_SIZE = 2
SNAKE_COLOR = '#FFFFFF'
FOOD_COLOR = '#FF0000'


class Snake:
    def __init__(self):
        self.coordinates = []

        for i in range(0, DEFAULT_BODY_SIZE):
            x = (i + 2) * CELL_SIZE
            y = 4 * CELL_SIZE
            self.coordinates.append([x, y])
            canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=SNAKE_COLOR)

        self.generate_food()

    def generate_food(self):
        while True:
            x = random.randint(0, WIDTH - 1) * CELL_SIZE
            y = random.randint(0, WIDTH - 1) * CELL_SIZE
            coordinate = [x, y]
            if coordinate not in self.coordinates:
                canvas.create_oval(
                    x,
                    y,
                    x + CELL_SIZE,
                    y + CELL_SIZE,
                    fill=FOOD_COLOR,
                )
                return coordinate


window = tk.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tk.Canvas(window, width=WIDTH * CELL_SIZE, height=HEIGHT * CELL_SIZE, bg="black")
canvas.pack()

snake = Snake()

window.mainloop()
