# Cellular automaton
In this chapter we will create a game without players. We will create **cellular automatons**.

A cellular automaton is a simplified world consisting of identical cells which have two states: dead or alive.

Instead of players interacting with our cells we will apply simple rules to each cell. Depending on the number of alive neighbours of the current cell and the applied rules the cell state will change (e.g. from living to dead or vice versa). 

So for these kind of games we only need these things:

    - a game board
    - cells with two states (alive and dead)
    - game rules applied to the cells of the board

In the simplest case the board is 1-dimensional. In the following picture we have a 1-dimensional board of length 10:
![Population at t_0](ressources/t0.png "Population at t_0")

This is our current *population*. 
At time point `t_0` every cell is dead except the fifth cell (`idx 4`)

Now let's apply some simple rules. Let's say the next population emerges from the current population, but every cell which is dead in the current population will become alive in the next population and every cell alive in the current population will be dead in the next.

Or expressed in a table:

| Current state | Next state |
|---------------|------------|
|    DEAD       |  ALIVE     | 
|    ALIVE      |  DEAD      | 

This will lead to the following population:
![Population at t_1](ressources/t1.png "Population at t_1")

If we apply the rules multiple times the states will toggle back and furth. 
![Population at t_2](ressources/t2.png "Population at t_2")

So these toggling of cell states is kind of boring. Let's apply some more interesting rules. 

## Rule 90
In our previous example the state of the next cell only depends on the state of the current cell. The state of adjacent cells was not relevant.

Let's change this by inspecting not only the state of the current cell, but also the state of the direct adjacent neighbours. 

A dead cell is represented by a 0, while a living cell is represented by a 1.
So if we inspect 3 cells at once we get 8 combinations of living and dead cells (`2**3`).
We will now apply the following rules:

| Current state | Next state |
|---------------|------------|
| 111           |  0         | 
| 110           |  1         | 
| 101           |  0         | 
| 100           |  1         | 
| 011           |  1         | 
| 010           |  0         | 
| 001           |  1         | 
| 000           |  0         | 

We will skip the cell with index 0 on the left edge of our 1-dimensional board because it has no left neighbour. Instead we start with index 1. The red box emphasizes the 3 cells we are currently looking at.

![Rule 90 at t_0](ressources/rule90_t_0_idx1.png "Rule 90 at t_0")

The next population is currently under construction. For the left outer cell we will use a dead cell and so we add a dead cell for index 0 in `t_1`.

Let's now have a look at the 3 cells with index 0-2. Our 3-cell-state for cell with index 1 is `000`. We look the current state pattern up in our Rule 90 table and see in the last row that `000` will map to `0` as the next cell state and so we add a dead cell again.

Our intermediate result looks like this:
![Rule 90 at t_1 under construction](ressources/rule90_t_1_idx1.png "Rule 90 at t_1 under construction")

If we proceed with index 2 we also have only dead cells in the direct neighbourhood, so cell with index 2 of the next population is also dead.

It gets more interessting if we proceed with cell with index 3. Here we have the pattern `001` which will lead to a living cell. 
![Rule 90 at t_1 under construction](ressources/rule90_t_1_idx3.png "Rule 90 at t_1 under construction")

Cell with index 4 has pattern `010`. For this pattern the Rule 90 table results in a dead cell. Cell with index 5 has a pattern of `100` and this will result in a living cell. For the rest we only have zeros and therefore dead cells. So if we apply Rule90 to every cell we get the following result of the next population:

![Rule 90 at t_1 under construction](ressources/rule90_t_1.png "Rule 90 at t_1 under construction")

To get our next population we continue this procedure but use the population of `t_1` as a basis to apply the rules and create population `t_2`. 

# Implementation in Python
The procedure of creating new populations out of existing populations is clear now. How can we implement this in Python?

We use the *top-down approach* for this by dividing the problem of cellular automaton into several smaller subproblems. These subproblems are:

    - Defining a cell with state DEAD and ALIVE
    - Finding an appropriate data structure to represent our 1-dimensional game board with our cells
    - Defining the rules
    - Finding an appropriate representation for our output
    - Implementing the control flow

Let's start with the cell itself.

## Cells
A cell has only two states: DEAD or ALIVE. So as in the rules above it may be obvious to use a `0` for a dead cell and a `1` for a living cell.

If we change the cell state from dead to alive we change the value from `0` to `1` and vice versa.

## Data structure for a 1-dimensional game board
For a 1-dimensional game board an Python `array` may be a good data structure. 

An array is very similar to a list. The behaviour is nearly identical, but we have to specifiy the type of object we can store in them. Remember: we can store different types of objects like `ints`, `floats`, `functions` or `strings` in lists. But in our case we only want to store single characters: in particular `'1'` for a living cell, and `'0'` for a dead cell. 

Using an array not only saves us memory, but also avoiding adding non compliant types by accident.

``` python
# to use arrays we have to import them
import array

board_width=20

# the 'u' specifies that we want to store (unicode) characters
# we initialize the array with only zeros (a string with in this case 20 zeros)
board = array.array('u', "0"*board_width)
``` 

## Defining the game rules
Let us implement the game rules. If you look at the table above the first thing that comes to your mind is using a dictionary as a lookup for the game rules. 

Using a dictionary for this is actually quite simple and expresses the intentaion of the game rules quit clearly. Look how similar the Python dictionary looks to our table.

``` python
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
```

## Representation
We start very simple and only print our results to the console. We do not use a graphical user interface (GUI) module for our output.

For that it may be sufficient to print a string which represents our current population. An dead cell is represented by "nothing", so just a space and a dead cell is printed by a character which is mostly filled, e.g. '#' (a hashtag).

Let's have a look at how we may print our current population.
``` python
import array

# we have a board of length 12
board = array.array('u', '001101011011')

current_population = "".join(board)
print(current_population)   # will output '001101011011'
```
Wait! This is not what we want. We want to have spaces instead of `0` and `#` instead of `1`. 

One way to do this is to replace every occurence in the string.
``` python
import array

# we have a board of length 12
board = array.array('u', '001101011011')

current_population = "".join(board)
current_population = current_population.replace('0', ' ')
current_population = current_population.replace('1', '#')
print(current_population)   # will output as expected :)
```
Remember: A string is immutable so we cannot change the string in place. Calling method `replace` will give us back a new string with each occurence replaced and we bind the name `current_population` to that new string.

An alternative to create our output string is to use the ternary operator in a generator expression in Python.
``` python
import array

# we have a board of length 12
board = array.array('u', '001101011011')

current_population = "".join( '#' if char == '1' else ' ' for char in board)
print(current_population)   # will output as expected :)
```

## Control flow


# Other rules

## Rule 30

## Rule 80

# Game of Life

Trivia: In the early 1970s the game was so popular, that the us army estimated the costs of consumed computing time by the game to several millions of dollars. 

# Additional Ressources
https://www.youtube.com/watch?v=DUfdBdrK2ag