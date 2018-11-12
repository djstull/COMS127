# David James Kay Stull
# Com Sci 127

import numpy as np


def empty_plane(x, y):
    return np.full((y, x), False)


def seed_plane_position(plane, x, y):
    plane[y-1, x-1] = True
    return world


def seed_plane(plane):
    pass


def print_plane(plane):
    plane[plane is False] = 0
    return plane


world = empty_plane(4, 4)
# empty_plane test - COMPLETE
# print(empty_plane(5, 4))

# seed_plane_position - COMPLETE
# print(seed_plane_position(world, 4, 4))

print(print_plane(world))