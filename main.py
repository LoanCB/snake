import tkinter as tk

WIDTH = 10
HEIGHT = 10
CELL_SIZE = 50
SPEED = 200
DEFAULT_BODY_SIZE = 2
SNAKE_COLOR = '#FFFFFF'


class Snake:
    def __init__(self):
        self.body_size = DEFAULT_BODY_SIZE
        self.coordinates = []
        self.squares = []

        for i in range(0, self.body_size):
            self.coordinates.append([i + 2, 4])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x * CELL_SIZE,
                y * CELL_SIZE,
                x * CELL_SIZE + CELL_SIZE,
                y * CELL_SIZE + CELL_SIZE,
                fill=SNAKE_COLOR
            )
            self.squares.append(square)


window = tk.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tk.Canvas(window, width=WIDTH * CELL_SIZE, height=HEIGHT * CELL_SIZE, bg="black")
canvas.pack()

snake = Snake()

window.mainloop()
