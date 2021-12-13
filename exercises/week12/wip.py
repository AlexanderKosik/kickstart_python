import time
import copy
import array

# create a board with a length of 100
# initialize everything with zeros, except of the cell in the middle
length = 500
population = array.array('u', '0'*length)
population[249] = '1'


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

rule_30 = {
    '111': '0', 
    '110': '0', 
    '101': '0', 
    '100': '1', 
    '011': '1', 
    '010': '1', 
    '001': '1', 
    '000': '0', 
}

def new_population(current_population):
    """
    This method creates a new population out of the passed current_population
    """ 
    # copy the current_population for our new population
    new_population = copy.deepcopy(current_population)

    # let's iterate over the current_population
    # (without the outer left and outer right edge)
    for index, _ in enumerate(current_population[1:-1], start=1):
        # use a slice to get adjacent cells
        start_index = index - 1

        # Why do we use index + 2?
        # Experiment with list slicing if you are unsure
        end_index = index + 2 
        cell_slice = current_population[start_index:end_index]

        # convert the cell slice to a string. (We have already done this,
        # scroll up if unsure how to do this)
        # Attention: Do not convert to the output format here!
        pattern = "".join(cell_slice)

        # look the pattern up in our rule. It is a normal dictionary lookup
        result = rule_30[pattern]

        # set the result in the new_population
        new_population[index] = result

    # we are done. Let's return the new_population
    return new_population

while True:
    # convert the population to a string 
    # do the replacement of the output format here
    output_string = "".join(population)
    output_string = output_string.replace('0', ' ')
    output_string = output_string.replace('1', '#')

    # print the current population
    print(output_string)

    # calculate new population
    population = new_population(population)

    # let's sleep a little bit. This will print 4 lines per second.
    # Adjust if desired
    time.sleep(0.05)