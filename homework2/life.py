# David James Kay Stull
# Computer Science 127

# This script contains the code for running the simulation for Conway's Game of Life.
# The other script includes the logic code for the simulation. I separated them for ease of
# use and to help with organization during programming.

# This script has the run_timestep, seed_plane_position, run_timestep, and play_life functions.
# The other required functions are inside environment.py.

from environment import Environment
from time import sleep
import random
import copy


# Allows user to set size of environment
def set_size(rws, clmns):
    global x, y, env
    x = rws
    y = clmns
    env = Environment(x, y)


# Run the simulation one time/
def run_timestep():
    old_env = copy.copy(env)
    for i in range(len(old_env.matrix)):
        for n in range(len(old_env.matrix[0])):
            if old_env.count_neighbors(i, n) < 2 or old_env.count_neighbors(i, n) > 3:
                env.set_dead(i, n)
            elif not old_env.alive[(i, n)] and old_env.count_neighbors(i, n) == 3:
                env.seed_plane(i, n)
    env.print_plane()


# Generates a random initial state of alive and dead cells
def generate():
    for i in range(x):
        for n in range(y):
            if random.choice([True, False]):
                env.seed_plane(i, n)
    env.print_plane()


# Change plane values to True / alive
def seed_plane_position(*positions):
    for p in positions:
        env.seed_plane(*p)
    env.print_plane()


# Runs the Game of Life
def play_life():
    xcord = input("Please input the dimension (x) for the grid: ")
    ycord = input("Please input the dimension (y) for the grid: ")
    xcord = int(xcord)
    ycord = int(ycord)

    set_size(xcord, ycord)

    times = input("How many times should the simulation be ran?: ")
    times = int(times)

    t = -1
    while True:
        if t == -1:
            generate()
        else:
            run_timestep()
        t += 1
        times -= 1
        sleep(1)
        if times <= 0:
            break

# You can run the game using the play_life():
play_life()