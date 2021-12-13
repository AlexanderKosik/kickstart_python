import os
import time
import random
import copy
import collections

# create a board with 20 x 100
width = 150
height = 40

board = [['0' for _ in range(width)] for _ in range(height)]

# add earth
board[-1] = ['1' for _ in range(width)]

# add seads with a percentage of 10 percent
board[-2] = ['1' if random.random() < 0.1 else '0' for _ in range(width)]
board[-3] = board[-4] = board[-2]

symbols = collections.defaultdict(lambda: '$')
symbols[height-1] = "#"
symbols[height-2] = "."
symbols[height-3] = "|"
symbols[height-4] = "|"

rule_90 = {
    '111': '0', 
    '110': '1', 
    '101': '0', 
    '100': '1', 
    '011': '1', 
    '010': '0', 
    '001': '1', 
    '000': '0', 
}

def print_board(board):
    """
    print the board.
    Therefore the clean must be cleared before. To this with a system 'cls' command
    """ 
    # clear the screen
    os.system('cls')

    # print our board
    for line_number, row in enumerate(board):
        output_line = "".join(row)
        output_line = output_line.replace("1", symbols[line_number])
        output_line = output_line.replace("0", " ")
        print(output_line)

def new_population(current_population):
    """
    This method creates a new population out of the passed current_population
    """ 
    # copy the current_population for our new population
    new_population = copy.deepcopy(current_population)

    # let's iterate over the current_population (without the outer left and outer right edge)
    for index, _ in enumerate(current_population[1:-1], start=1):
        # use a slice to get adjacent cells
        start_index = index - 1
        end_index = index + 2 # Why do we use index + 2? Experiment with list slicing if you are unsure
        cell_slice = current_population[start_index:end_index]

        # convert the cell slive to a string. (We have already done, so scroll up if unsure)
        # Attention: Do not convert to the output format here!
        pattern = "".join(cell_slice)

        # look the pattern up in our rule. It is a normal dictionary lookup
        result = rule_90[pattern]

        # set the result in the new_population
        new_population[index] = result

    # we are done. Let's return the new_population
    return new_population


current = 36

while True:
    print_board(board)

    new_pop = new_population(board[current])
    current -= 1
    board[current] = new_pop
    # let's sleep a little bit. This will print 4 lines per second.
    # Adjust if desired
    time.sleep(0.5)

    if current == 0:
        break