import tkinter as tk
from random import randrange


class minesweeper:
    def __init__(self, window, difficulty="easy"):
        self.window = window
        self.window.title("Minesweeper")
        self.bombs = 15

        self.rows, self.columns = self.set_difficulty(difficulty)

        self.tiles = self.create_tiles()
        self.bomb_tiles = self.set_bombs(self.tiles)

        self.to_win = self.rows * self.columns - len(self.bomb_tiles)
        self.is_game_over = False
        self.indicators = []
        self.revealed = []

        self.set_indicators()

    def set_difficulty(self, val):
        if val == "easy":
            return 10, 10

    def create_tiles(self):
        tiles = []
        rows = self.rows
        cols = self.columns

        # Playing field
        x = 0
        while x < cols:
            y = 0
            buttons = []
            while y < rows:
                buttons.append(tk.Label(text="", bg="green", height="2", width="4", borderwidth=5, relief="raised"))
                buttons[y].bind("<Button-1>", self.left_click)
                buttons[y].bind("<Button-2>", self.right_click)
                buttons[y].grid(row=x, column=y)
                y += 1
            tiles.append(buttons)
            x += 1
        return tiles

    def right_click(self, event):
        if not self.is_game_over:
            column = event.widget.grid_info()["column"]
            row = event.widget.grid_info()["row"]

            if[row,column] not in self.revealed:
                event.widget.config(text="X")

    def left_click(self, event):
        if not self.is_game_over:
            column = event.widget.grid_info()["column"]
            row = event.widget.grid_info()["row"]
            self.reveal(row, column)
            if len(self.revealed) == self.to_win:
                self.you_win()

    def reveal(self, row, column):
        if [row, column] not in self.revealed:
            if [row, column] in self.bomb_tiles:
                # self.tiles[row][column].config(bg="pink")
                self.game_over()
                # self.window.destroy()
            elif [row, column] in self.indicators:
                self.color_indicators(row, column)
                self.revealed.append([row, column])
            elif [row, column] not in self.bomb_tiles and [row, column] not in self.indicators:
                self.tiles[row][column].config(bg="#a1776a", relief="ridge")
                self.revealed.append([row, column])
                self.check_adjacent_tiles(row, column, self.reveal)

    def check_adjacent_tiles(self, row, column, func):
        r = row
        c = column
        if row == 0 and column == 0:
            func(row, column + 1)
            func(row + 1, column)
            func(row + 1, column + 1)
        elif row == 9 and column == 9:
            func(row - 1, column)
            func(row - 1, column - 1)
            func(row, column - 1)
        elif row == 0 and column == 9:
            func(row, column - 1)
            func(row + 1, column - 1)
            func(row + 1, column)
        elif row == 9 and column == 0:
            func(row - 1, column)
            func(row - 1, column + 1)
            func(row, column + 1)
        elif row == 0:
            func(row, column - 1)
            func(row, column + 1)
            func(row + 1, column - 1)
            func(row + 1, column)
            func(row + 1, column + 1)
        elif row == 9:
            func(row - 1, column)
            func(row - 1, column - 1)
            func(row - 1, column + 1)
            func(row, column - 1)
            func(row, column + 1)
        elif column == 0:
            func(row - 1, column)
            func(row - 1, column + 1)
            func(row, column + 1)
            func(row + 1, column)
            func(row + 1, column + 1)
        elif column == 9:
            func(row - 1, column)
            func(row - 1, column - 1)
            func(row, column - 1)
            func(row + 1, column - 1)
            func(row + 1, column)
        else:
            func(row - 1, column)
            func(row - 1, column - 1)
            func(row - 1, column + 1)
            func(row, column - 1)
            func(row, column + 1)
            func(row + 1, column - 1)
            func(row + 1, column)
            func(row + 1, column + 1)

    def set_bombs(self, tiles_list):
        num_of_bombs = self.bombs
        bomb_tiles = []
        bombs_planted = 0

        while bombs_planted < num_of_bombs:
            row = randrange(10)
            col = randrange(10)
            if [row, col] not in bomb_tiles:
                # tiles_list[row][col].config(bg="purple")
                bomb_tiles.append([row, col])
                bombs_planted += 1
        return bomb_tiles

    def set_indicators(self):
        for bomb in self.bomb_tiles:
            self.check_adjacent_tiles(bomb[0], bomb[1], self.get_indicators)

    def get_indicators(self, row, column):
        if [row, column] not in self.bomb_tiles:
            self.indicators.append([row, column])

    def color_indicators(self, row, column):
        count = self.indicators.count([row, column])
        if count == 1:
            self.tiles[row][column].config(text=count, fg="yellow", bg="#a1776a", relief="ridge")
        elif count == 2:
            self.tiles[row][column].config(text=count, fg="orange", bg="#a1776a", relief="ridge")
        elif count == 3:
            self.tiles[row][column].config(text=count, fg="red", bg="#a1776a", relief="ridge")
        elif count == 4:
            self.tiles[row][column].config(text=count, fg="#fc3503", bg="#a1776a", relief="ridge")
        elif count == 5:
            self.tiles[row][column].config(text=count, fg="#fc0303", bg="#a1776a", relief="ridge")
        elif count == 6:
            self.tiles[row][column].config(text=count, fg="#1403fc", bg="#a1776a", relief="ridge")
        elif count == 7:
            self.tiles[row][column].config(text=count, fg="black", bg="#a1776a", relief="ridge")

    def game_over(self):
        self.is_game_over = True
        for bomb in self.bomb_tiles:
            self.tiles[bomb[0]][bomb[1]].config(bg="red")
        new_game(self.window, "Game Over")
        # try_again = tk.Tk()
        # game_over = new_game(try_again, "try_again?")
        # self.window.destroy()

    def you_win(self):
        new_game(self.window, "YOU WIN!")


def new_game(window, message):
    new_window = tk.Toplevel(window)
    msg = tk.Label(new_window, text=message)
    msg.grid(row=0, column=0, columnspan=2, pady=5, padx=5)
    label = tk.Label(new_window, text="Try again?")
    label.grid(row=1, column=0, columnspan=2, pady=5, padx=5)
    button_yes = tk.Button(new_window, text="Yes", command=lambda: retry_game(window))
    button_yes.grid(row=2, column=0, columnspan=1, pady=5, padx=5)
    button_no = tk.Button(new_window, text="No", command=lambda: quit_game(window))
    button_no.grid(row=2, column=1, columnspan=1, pady=5, padx=5)


def quit_game(window):
    root.destroy()


def retry_game(window):
    window.destroy()
    root = tk.Tk()
    start = minesweeper(root)
    root.mainloop()


root = tk.Tk()
start = minesweeper(root)
root.mainloop()
