# David James Kay Stull
# Com Sci 127

import sys
import time
import numpy as np


def empty_plane(x, y):
    world = np.full((y, x), False).reshape(y, x)
    return world


def seed_plane_position(plane, x, y):
    plane[y-1, x-1] = True
    return plane


def seed_plane(plane):
    answer = ""
    while answer != "EOF":
        answer = input("Please input the coordinates you wish to change. Type EOF when finished.: ")
        if answer == "EOF":
            world = world
            pass
        else:
            answer = answer.split()
            cordx = int(answer[0])
            cordy = int(answer[1])
            world = seed_plane_position(plane, cordx, cordy)
            print(world)
    return world


def print_plane(plane):
    plane = plane.astype(str)
    plane[plane == "True"] = "o"
    plane[plane == "False"] = " "

    return plane


def count_neighbors(plane, x, y):
    neighbors = 0
    for hor in [x-1, x, x+1]:
        for ver in [y-1, y, y+1]:
            if not hor == ver == "o" and (plane == "o" or (0 <= x + hor < x and 0 <= y + ver < y)):
                neighbors += plane[(y + ver) % y][(x + hor) % x]
    return neighbors


def play_life():
    x = input("Please input the X dimension for the world: ")
    y = input("Please input the Y dimension for the world: ")
    x = int(x)
    y = int(y)
    steps = input("How many times should the simulation be ran?: ")
    world = empty_plane(x, y)
    world = seed_plane(world)
    world = print_plane(world)
    neighbors = count_neighbors(world, 1, 1)
    print(neighbors)
    print(world)

# empty_plane test - COMPLETE
# print(empty_plane(10, 10))

# seed_plane_position - COMPLETE
# print(seed_plane_position(world, 4, 4))

# seed_plane - INCOMPLETE - NEEDS TO TAKE TXT INPUT
# print(seed_plane(world))

# print_plane - COMPLETE
# print(print_plane(world))

# count_neighbors
# print(count_neighbors(world, 1, 1))


# play_life - INCOMPLETE
play_life()

