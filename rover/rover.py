from .constants import (
    HEADING_NORTH,
    HEADING_SOUTH,
    HEADING_EAST,
    DIRECTIONS
)
from collections import namedtuple

Coords = namedtuple('Coords', ['x', 'y'])


class Rover(object):
    """ An encapsulation of the mars vehicle
    """

    def __init__(self, x=0, y=0, heading=HEADING_NORTH, plateau=None):
        self.x = x
        self.y = y
        self.heading = heading
        self.plateau = plateau
