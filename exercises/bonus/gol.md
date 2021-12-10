# Game of Life

The Game of Life is a 2-dimensional game without players. We have already created most of the components we need for the game in the previous chapter. 

For example:

- The 2-dimensional game board with cells
- The output of a 2-dimensional game board

![Game of Life](ressources/gol.png "Game of Life")

The Game of Life consists of four simple rules, but their application makes our board come to life in incredible ways. Let's have a look how these rules are defined.

## Game rules
As before we calculate the next population using the current one. But the rules are a little bit different now. 

To calculate the next population we start with the number of alive neighbours of the current cell under inspection. Most cells (except the cells on the edge of the board) have exactly 8 neighbours. 

![4 Game Rules](ressources/gol_rules.png "The 4 game rules")

Let's have a look at the four rules in detail.

### 1. Underpopulation
If a living cell has less than 2 living neighbours the cell is dead in the next population because of underpopulation.

### 2. Stay alive
If a living cell has exactly 2 or 3 living neighbours it will stay alive in the next population. 

### 3. Overcrowding
If a living cell has more than 3 living neighbours it will be dead in the next population because of overcrowding

### 4. Resurrection
If a living cell is dead in the current population but has exactly 3 living neighbours it will be resurrected and be alive in the next population.

## Calculating the number of alive neighbours

Trivia: In the early 1970s the game was so popular, that the us army estimated the costs of consumed computing time by the game to several millions of dollars. 

# Additional Ressources
If you want so see a short introduction into Game of Life of Cellular automaton, have a look at this video. (you can enable subtitles if needed)
https://www.youtube.com/watch?v=DUfdBdrK2ag