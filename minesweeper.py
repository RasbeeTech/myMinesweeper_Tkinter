import tkinter as tk
from random import randrange


def right_click(event):
    print("Right click")
    event.widget.config(bg="red")
    print("row:", event.widget.grid_info()["row"])
    print("col:", event.widget.grid_info()["column"])


def left_click(event):
    print("Left click")
    event.widget.config(bg="white")
    print(event.widget.grid_info())
    print("row:", event.widget.grid_info()["row"])
    print("col:", event.widget.grid_info()["column"])
    # print(randrange(10),randrange(10))


def set_bombs():
    print("Setting bombs")
    bombs = 0
    bomb_tiles = []
    while bombs < 10:
        row = randrange(10)
        col = randrange(10)
        if [row, col] not in bomb_tiles:
            bomb_tiles.append([row, col])
            bombs += 1

    print("bombs:", bomb_tiles)


if __name__ == '__main__':
    window = tk.Tk()
    window.title("Minesweeper")

    rows = 10
    cols = 10
    x = 0
    y = 0

    tiles = []
    while x < cols:
        y = 0
        buttons = []
        while y < rows:
            print(x, y)
            buttons.append(tk.Label(text=(x, y), bg="purple", height="3", width="6", borderwidth=5, relief="raised"))
            buttons[y].bind("<Button-1>", left_click)
            buttons[y].bind("<Button-2>", right_click)
            buttons[y].grid(row=x, column=y)
            y += 1
        tiles.append(buttons)
        x += 1
    print(tiles)
    for i in tiles:
        print(i[1].grid_info())
        i[1].config(bg="green")
    # button = tk.Button(height="3",width="6", bd=5, bg="red").grid(row="0", column="10")
    print("mainloop")
    set_bombs()
    window.mainloop()
