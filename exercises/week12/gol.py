import random
import time
import copy
import os
import sys
import re

#######
# BOARD
#######
# Let's create and initialize the board by random
# 4/5 of all cells are dead in our start configuration
width = 200
height = 100
board = [[0 if random.random() < 0.8 else 1 for _ in range(width)] for _ in range(height)]
DEAD = 0
ALIVE = 1

#################
# Neighbour count
#################
def alive_neighbours(board, cell_coordinate: tuple) -> int:
    """
    Returns the number of alive neighbours
    """
    # unpack the tuple
    x, y = cell_coordinate

    # We do not want to have 'from_values' below 0, therefore we use min
    # We do not want to have 'to_values' above our max width/height
    # Pay attention: last valid width index is width -1
    # Pay attention: last valid height index is height -1
    x_from, x_to = max(x-1, 0), min(x+1, width -1)
    y_from, y_to = max(y-1, 0), min(y+1, height -1)

    # lets write the nested for loop as a comprehension and use builtin function sum
    alive_cells = sum(board[y][x] 
        for y in range(y_from, y_to +1)
        for x in range(x_from, x_to +1))

    # reduce by cell state of CUI
    alive_cells -= board[y][x] 
    return alive_cells

<<<<<<< HEAD:exercises/bonus/gol.py
def alive_neighbours_sphere(board, cell_coordinate: tuple) -> int:
=======
def alive_neighbours(board, cell_coordinate: tuple) -> int:
>>>>>>> 00be2838fce09317ce3178fae08fefe13135787d:exercises/week12/gol.py
    """
    Returns the number of alive neighbours on a spherical game board 
    """
    # unpack the tuple
    x, y = cell_coordinate

    x_from, x_to = x-1, (x+1) % width
    y_from, y_to = y-1, (y+1) % height

    # Access the items individually and sum them up 
    # (sum needs an iterable, so we create a temporary list, without the CUI)
    alive_cells = sum([
        board[y_from][x_from], board[y_from][x],board[y_from][x_to],
        board[y][x_from],                       board[y][x_to],
        board[y_to][x_from],   board[y_to][x],  board[y_to][x_to],
    ])

    return alive_cells 
#################
# Game Rules
#################
def game_rules(nalive, cui_state):
    game_rules = {
        0: DEAD, 
        1: DEAD, 
        2: ALIVE, 
        3: ALIVE, 
        4: DEAD, 
        5: DEAD, 
        6: DEAD, 
        7: DEAD, 
        8: DEAD, 
    }
    next_state = game_rules[nalive]
    if nalive == 2:
        next_state &= cui_state
    return next_state


#################
# Print the game board
#################
def print_board(board):
    """
    Prints the passed game board. Must be a list of a list.
    Therefore the screen must be cleared before. Do this with a system 'cls'
    command (windows) or 'clear' on unix
    """ 
    # clear the screen
    os.system('cls')

    # print our board
    for row in board:
        output_line = "".join(str(cell) for cell in row)

        # Fix this: we need to replace 1s and 0s with a valid symbols
        output_line = output_line.replace("1", "x")
        output_line = output_line.replace("0", " ")
        print(output_line)


def init_board(filename):
    global board
    board = [[0 for _ in range(width)] for _ in range(height)]
    y = height // 2
    x = width // 2
    with open(filename) as f:
        current_row = y
        for row in f:
            if not row.startswith("!"):
                for offset, cell in enumerate(row):
                    if cell == "O":
                        board[current_row][x+offset] = 1
                current_row += 1


calc_alive_neigh_func = alive_neighbours_sphere

for arg in sys.argv:
    if re.search(r"\.cells", arg):
        init_board(arg)

#################
# Game Loop
#################
while True:
    # print the current population
    print_board(board)

    # copy the board for the next generation
    next_gen = copy.deepcopy(board)

    # update every cell for our next generation
    for x in range(width):
        for y in range(height):
            alive_neighbour_count = calc_alive_neigh_func(board, (x, y))
            next_gen[y][x] = game_rules(alive_neighbour_count, board[y][x])
    
    # use next_gen as current_gen for next iteration
    board = next_gen

    # adjust to your demands
    time.sleep(0.02)
