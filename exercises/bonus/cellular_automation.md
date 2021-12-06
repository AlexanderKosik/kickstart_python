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

We will use a dead cell for the cell on the left edge. Our 3-cell-state for cell with index 1 is `000`. We look the current state pattern up in our Rule 90 table and see in the last row that `000` will map to `0` as the next cell state (so we have a dead cell again).

So we have the following intermediate result:
![Rule 90 at t_1 under construction](ressources/rule90_t_1_idx1.png "Rule 90 at t_1 under construction")

If we proceed with index 2 we also have dead cells in the direct neighbourhood, so cell with index 2 of the next population is also dead.

It gets more interessting if we proceed with cell with index 3. Here we have the pattern `001` which will lead to a living cell. 
![Rule 90 at t_1 under construction](ressources/rule90_t_1_idx3.png "Rule 90 at t_1 under construction")

Cell with index 4 has pattern `010`. For this pattern the Rule 90 table results in a dead cell. Cell with index 5 has a pattern of `100` and this will result in a living cell. For the rest we only have zeros and therefore dead cells. So if we apply Rule90 to every cell we get the following result of the next population:

![Rule 90 at t_1 under construction](ressources/rule90_t_1.png "Rule 90 at t_1 under construction")


## Rule 30

## Rule 80

# Game of Life

Trivia: In the early 1970s the game was so popular, that the us army estimated the costs of consumed computing time by the game to several millions of dollars. 

# Additional Ressources
https://www.youtube.com/watch?v=DUfdBdrK2ag