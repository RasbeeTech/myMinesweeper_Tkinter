import tkinter as tk
import random
from random import randrange


class minesweeper:
    def __init__(self, window):
        self.window = window
        self.window.title("Minesweeper")
        self.tiles = self.create_tiles()
        self.bomb_tiles = self.set_bombs(self.tiles)

    def create_tiles(self):
        tiles = []
        rows = 10
        cols = 10
        x = 0
        y = 0
        while x < cols:
            y = 0
            buttons = []
            while y < rows:
                print(x, y)
                buttons.append(tk.Label(text=(x, y), bg="green", height="2", width="4", borderwidth=5, relief="raised"))
                buttons[y].bind("<Button-1>", self.left_click)
                buttons[y].bind("<Button-2>", self.right_click)
                buttons[y].grid(row=x, column=y)
                y += 1
            tiles.append(buttons)
            x += 1
        return tiles

    def right_click(self, event):
        print("Right click")
        event.widget.config(bg="red")
        print("row:", event.widget.grid_info()["row"])
        print("col:", event.widget.grid_info()["column"])

    def left_click(self, event):
        print("Left click")
        event.widget.config(bg="white")
        print(event.widget.grid_info())
        # print(randrange(10),randrange(10))
        column = event.widget.grid_info()["column"]
        row = event.widget.grid_info()["row"]
        self.check_tiles(row,column)

    def check_tiles(self,row,column):
        r = row
        c = column
        print(self.tiles[row][column].grid_info())
        self.tiles[row-1][column].config(bg="blue")


    def set_bombs(self, tiles_list):
        print("Setting bombs")
        num_of_bombs = 10
        bomb_tiles = []
        bombs_planted = 0

        while bombs_planted < num_of_bombs:
            row = randrange(10)
            col = randrange(10)
            if [row, col] not in bomb_tiles:
                tiles_list[row][col].config(bg="red")
                print(tiles_list[row][col].grid_info())
                bomb_tiles.append([row, col])
                bombs_planted += 1

        print("bomb_tiles:", bomb_tiles)
        print("bombs: ", len(bomb_tiles))
        return bomb_tiles


if __name__ == '__main__':
    window = tk.Tk()
    start = minesweeper(window)
    window.mainloop()
    '''for i in tiles:
        for k in i:
            print("row:", k.grid_info())
            if (k.grid_info()["row"] % 2) == 0:
                k.config(bg="orange")
        # print(i[1].grid_info())
        i[1].config(bg="green")'''
