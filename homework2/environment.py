# David James Kay Stull
# Computer Science 127

# This is the script with the logic for the Conway's Game of Life Simulation.

# The seed_plane, print_plane, and count_neighbors required functions are in this script.

import os


class Environment:

    # Creates empty plane / environment with all cells dead / set to false.
    # This is my empty plane.
    def __init__(self, x, y):
        self.matrix = []
        self.alive = {}
        for i in range(x):
            r = []
            for n in range(y):
                r.append(' ')
                self.alive[(i, n)] = False
            self.matrix.append(r)

    # Sets a cell to alive / true.
    # This is my seed plane.
    def seed_plane(self, x, y):
        self.matrix[x][y] = 'o'
        self.alive[(x, y)] = True

    # Sets a cell to dead / false.
    def set_dead(self, x, y):
        self.matrix[x][y] = ' '
        self.alive[(x, y)] = False

    # Prints the game plane / environment.
    def print_plane(self):
        os.system('cls')
        for i in range(len(self.matrix)):
            for n in range(len(self.matrix[i])):
                print(self.matrix[i][n], end=' ')
            print()

    # Returns the number of neighbors that are alive / true.
    def count_neighbors(self, x, y):
        neighbors = 0
        if x > 0 and self.alive[(x - 1, y)]:
            neighbors += 1
        if x < len(self.matrix) - 1 and self.alive[(x + 1, y)]:
            neighbors += 1
        if y > 0 and self.alive[(x, y - 1)]:
            neighbors += 1
        if y < len(self.matrix[0]) - 1 and self.alive[(x, y + 1)]:
            neighbors += 1
        if y > 0 and x > 0 and self.alive[(x - 1, y - 1)]:
            neighbors += 1
        if y < len(self.matrix[0]) - 1 and x > 0 and self.alive[(x - 1, y + 1)]:
            neighbors += 1
        if y > 0 and x < len(self.matrix) - 1 and self.alive[(x + 1, y - 1)]:
            neighbors += 1
        if y < len(self.matrix[0]) - 1 and x < len(self.matrix) - 1 and self.alive[(x + 1, y + 1)]:
            neighbors += 1
        return neighbors
