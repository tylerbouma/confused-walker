# random walk in a square grid-like pattern (2d-array)
# can move N, S, E, W
# monte carlo style testing will be used
import random

class Grid:
    def __init__(self, size=10):
        self.size = size

    def make_grid(self):
        self.grid = [[0 for x in range(self.size)] for y in range(self.size)]

    def print_grid(self):
        for v in self.grid:
            print(v)

directions = ['N', 'S', 'E', 'W']

def walk(grid):
    # count how many steps it takes to get to the edge
    # we know this by the size of the grid
    # start at position (0, 0)
    position = [0,0]
    try_attempts = 0
    avail_dirs = directions.copy()
    moved = True
    # keep going as long as you haven't hit one of the opposite edges
    while position[0] != len(grid)-1 and position[1] != len(grid[0])-1:
        # mark the current block as visited if we moved
        if moved == True:
            grid[position[0]][position[1]] += 1
            moved = False
        if position[0] == 0 or position[1] == 0:
            if 'N' in avail_dirs:
                avail_dirs.remove('N')
            if 'W' in avail_dirs:
                avail_dirs.remove('W')
        move = random.choice(avail_dirs)
        # only visit tiles that have not been visited before
        if move is 'N':
            if grid[position[0]-1][position[1]] != 1:
                position[0] -= 1
                avail_dirs = directions.copy()
                moved = True
            else:
                avail_dirs.remove('N')
        elif move is 'S':
            if grid[position[0]+1][position[1]] != 1:
                position[0] += 1
                avail_dirs = directions.copy()
                moved = True
            else:
                avail_dirs.remove('S')
        elif move is 'E':
            if grid[position[0]][position[1]+1] != 1:
                position[1] += 1
                avail_dirs = directions.copy()
                moved = True
            else:
                avail_dirs.remove('E')
        elif move is 'W':
            if grid[position[0]][position[1]-1] != 1:
                position[1] -= 1
                avail_dirs = directions.copy()
                moved = True
            else:
                # remove this option for the next move
                avail_dirs.remove('W')
        # if we have tried to move every way reset the grid
        if not avail_dirs:
            position=[0,0]
            reset_grid(grid)
            try_attempts+=1
            avail_dirs = directions.copy()
            moved = True
    
    grid[position[0]][position[1]] += 1
    print("Exited at %d, %d" % (position[0], position[1]))
    print("After %d tries." % try_attempts)

def reset_grid(grid):
    # reset all items on the grid to 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = 0

g = Grid(50)
g.make_grid()
walk(g.grid)
g.print_grid()
