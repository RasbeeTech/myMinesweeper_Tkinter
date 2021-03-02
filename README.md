# Minesweeper

 A simple 10x10 Minesweeper game
 
 Python version: 3.8.7

 TkInter is used to create the graphical user interface
 
 ## Sample:
 
 ![alt text](https://github.com/RasbeeTech/Minesweeper/blob/main/sample_image.jpeg)
 
 To see finished program code, click [here](https://github.com/RasbeeTech/Minesweeper/blob/main/minesweeper.py)
 
 ## Process:
 1.	Create a tkinter window.
 ```python
 import tkinter as tk
 
 root = tk.Tk() # Creates tkinter window
 root.mainloop() # Runs window
 ```
 2.	Create tkinter labels and arrange them using grid() (I accomplished this by using a nested while loop).
 		Note: Be sure to save labels where the can be accessed later.
 ```python
 tiles = []
 rows = 10
 cols = 10

 x = 0
 # A nested loop creates 2 dimensional array or a grid
 while x < cols:
 	y = 0
 	tile = []
 	# creates tiles by rows
 	while y < rows: 
 		# Labels serve as tiles for the game
 		tile.append(tk.Label(text="", bg="green", height="2", width="4", borderwidth=5, relief="raised"))
 		tile[y].bind("<Button-1>", left_click)
 		tile[y].bind("<Button-2>", right_click)
 		tile[y].grid(row=x, column=y)
 		y += 1
 	# adds the created row of row of labels to the tiles[]
 	tiles.append(tile)
 	x += 1
 ```
 3.	Bind left-click and right-click event functions to each label.
 		Left-click reveals() tile and adjacent tiles.
 		Right-click sets flags tile.
 ```python
 def right_click(event):
 	if not is_game_over:
        column = event.widget.grid_info()["column"]
        row = event.widget.grid_info()["row"]

        if[row,column] not in revealed:
            event.widget.config(text="X")
 def left_click(event):
	if not is_game_over:
		column = event.widget.grid_info()["column"]
        row = event.widget.grid_info()["row"]
        reveal(row, column)
        if len(revealed) == to_win:
            you_win()
 ```
 4. Using random number generator, get x and y locations to place mines.
 ```python
 from random import randrange
 
 def set_bombs():
    bomb_tiles = []
    bombs_planted = 0
	num_of_bombs = 10
	
	# Will set 10 mines on playing field in random locations
    while bombs_planted < num_of_bombs:
    	# randrange(10): randomly generates a integer between 0 and 9 to be used for location of mines
    	row = randrange(10)
        col = randrange(10)
        # If statement checks if mine is already placed in a location already
        if [row, col] not in bomb_tiles:
        	bomb_tiles.append([row, col])
        	bombs_planted += 1
 ```
 5. Create a function to check adjacent tiles.
 ```python
 # Takes location of a tile and applies function to all adjacent tiles
 def check_adjacent_tiles(row, column, func):
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
 ```
 6. Create function to set indicators for bomb locations when tile is revealed.
 ```python
 indicators = []
 
 def set_indicators():
    for bomb in bomb_tiles:
    # using method to check adjacent tiles the uses the get_idicators() function to add them to the indicators list.
    check_adjacent_tiles(bomb[0], bomb[1], get_indicators)
    
 def get_indicators(row, column):
 	# Make sure not to set indicators on top of a mine
	if [row, column] not in bomb_tiles:
    	indicators.append([row, column])
 ```
 7.	Finally, create actions for when the game is Win and Lose.
 ```python
 def game_over():
	is_game_over = True
	for bomb in bomb_tiles:
		tiles[bomb[0]][bomb[1]].config(bg="red")
    # new_game() is a function that makes a pop-up window that asks if you would like to try again
    new_game(window, "Game Over")
        
 def you_win():
	new_game(window, "YOU WIN!")
 ```
 	