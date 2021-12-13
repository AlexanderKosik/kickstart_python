import array
import time
import copy

# create a board with a length of 100
length = 100
# initialize everything with zeros, except of the cell in the middle

population = array.array('u', '0'*length)
population[50] = '1'

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

while True:
    # convert the population to a string 
    # do the replacement of the output format here
    output_string = "".join( '#' if char == '1' else ' ' for char in population)

    # print the current population
    print(output_string)

    # calculate new population
    population = new_population(population)

    # let's sleep a little bit. This will print 4 lines per second.
    # Adjust if desired
    time.sleep(0.25)
