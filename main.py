import tkinter as tk

WIDTH = 10
HEIGHT = 10
CELL_SIZE = 50
SPEED = 200
DEFAULT_BODY_SIZE = 2
SNAKE_COLOR = '#FFFFFF'


root = tk.Tk()
root.title("Snake")
root.resizable(False, False)

canvas = tk.Canvas(root, width=WIDTH * CELL_SIZE, height=HEIGHT * CELL_SIZE, bg="black")
canvas.pack()
root.mainloop()
