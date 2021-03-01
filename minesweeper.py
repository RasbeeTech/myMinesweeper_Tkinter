import tkinter as tk
import random
from random import randrange


class minesweeper:
    def __init__(self, window, difficulty="easy"):
        self.window = window
        self.window.title("Minesweeper")

        self.rows, self.columns = self.set_difficulty(difficulty)

        self.tiles = self.create_tiles()
        self.bomb_tiles = self.set_bombs(self.tiles)

        self.indicators = []
        self.revealed = []

        self.set_indicators()
    def set_difficulty(self, val):
        if val == "easy":
            return 10, 10
        if val == "medium":
            return 20, 20
        if val == "hard":
            return 30, 30

    def create_tiles(self):
        tiles = []
        rows = self.rows
        cols = self.columns

        x = 0
        while x < cols:
            y = 0
            buttons = []
            while y < rows:
                buttons.append(tk.Label(text=(x, y), bg="green", height="2", width="4", borderwidth=5, relief="raised"))
                buttons[y].bind("<Button-1>", self.left_click)
                buttons[y].bind("<Button-2>", self.right_click)
                buttons[y].grid(row=x, column=y)
                y += 1
            tiles.append(buttons)
            x += 1
        return tiles

    def right_click(self, event):
        event.widget.config(bg="red")
        print("row:", event.widget.grid_info()["row"])
        print("col:", event.widget.grid_info()["column"])

    def left_click(self, event):
        column = event.widget.grid_info()["column"]
        row = event.widget.grid_info()["row"]
        self.reveal(row, column)

    def reveal(self, row, column):
        if[row, column] not in self.revealed:
            if[row, column] in self.bomb_tiles:
                self.tiles[row][column].config(bg="pink")
            elif[row, column] in self.indicators:
                self.color_indicators(row,column)
                self.revealed.append([row, column])
            elif [row, column] not in self.bomb_tiles and [row, column] not in self.indicators:
                self.tiles[row][column].config(bg="white")
                self.revealed.append([row, column])
                self.check_adjacent_tiles(row, column, self.reveal)

    def check_adjacent_tiles(self, row, column, func):
        r = row
        c = column
        if row == 0 and column == 0:
            func(row,column+1)
            func(row+1,column)
            func(row+1, column+1)
        elif row == 9 and column == 9:
            func(row-1, column)
            func(row-1, column-1)
            func(row, column-1)
        elif row == 0 and column == 9:
            func(row, column-1)
            func(row+1, column-1)
            func(row+1, column)
        elif row == 9 and column == 0:
            func(row - 1, column)
            func(row - 1, column + 1)
            func(row, column + 1)
        elif row == 0:
            func(row, column-1)
            func(row, column+1)
            func(row+1, column-1)
            func(row+1, column)
            func(row+1, column+1)
        elif row == 9:
            func(row-1, column)
            func(row-1, column-1)
            func(row-1, column+1)
            func(row, column-1)
            func(row, column+1)
        elif column == 0:
            func(row-1, column)
            func(row-1, column+1)
            func(row, column+1)
            func(row+1, column)
            func(row+1, column+1)
        elif column == 9:
            func(row-1, column)
            func(row-1, column-1)
            func(row, column-1)
            func(row+1, column-1)
            func(row+1, column)
        else:
            func(row-1, column)
            func(row-1, column-1)
            func(row-1, column+1)
            func(row, column-1)
            func(row, column+1)
            func(row+1, column-1)
            func(row+1, column)
            func(row+1, column+1)

    def set_bombs(self, tiles_list):
        num_of_bombs = 10
        bomb_tiles = []
        bombs_planted = 0

        while bombs_planted < num_of_bombs:
            row = randrange(10)
            col = randrange(10)
            if [row, col] not in bomb_tiles:
                tiles_list[row][col].config(bg="purple")
                bomb_tiles.append([row, col])
                bombs_planted += 1
        return bomb_tiles

    def set_indicators(self):
        for bomb in self.bomb_tiles:
            self.check_adjacent_tiles(bomb[0], bomb[1], self.get_indicators)
        for i in self.indicators:
            count = self.indicators.count(i)
            self.tiles[i[0]][i[1]].config(text=count)

    def get_indicators(self, row, column):
        if [row, column] not in self.bomb_tiles:
            self.indicators.append([row, column])

    def color_indicators(self, row, column):
        count = self.indicators.count([row, column])
        if count == 1:
            self.tiles[row][column].config(text=count, bg="#e8fc03")
        elif count == 2:
            self.tiles[row][column].config(text=count, bg="#fcc203")
        elif count == 3:
            self.tiles[row][column].config(text=count, bg="#fc6703")
        elif count == 4:
            self.tiles[row][column].config(text=count, bg="#fc3503")
        elif count == 5:
            self.tiles[row][column].config(text=count, bg="#fc0303")
        elif count == 6:
            self.tiles[row][column].config(text=count, bg="#1403fc", fg="white")
        elif count == 7:
            self.tiles[row][column].config(text=count, bg="black", fg="white")


if __name__ == '__main__':
    window = tk.Tk()
    start = minesweeper(window)
    window.mainloop()
