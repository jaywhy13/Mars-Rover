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

    @property
    def coords(self):
        return Coords(self.x, self.y)

    @property
    def coords_after_move(self):
        """ If we move, what would the new coords be?
        """
        x = self.x
        y = self.y
        if self.heading == HEADING_NORTH:
            y += 1
        elif self.heading == HEADING_SOUTH:
            y -= 1
        elif self.heading == HEADING_EAST:
            x += 1
        else:
            x -= 1
        return Coords(x, y)

    def reset(self):
        """ Move the rover back to 0,0 and reset the heading
        """
        self.x = 0
        self.y = 0
        self.heading = HEADING_NORTH

    def turn_left(self):
        direction_index = DIRECTIONS.index(self.heading)
        new_direction_index = (direction_index - 1) % len(DIRECTIONS)
        self.heading = DIRECTIONS[new_direction_index]

    def turn_right(self):
        direction_index = DIRECTIONS.index(self.heading)
        new_direction_index = (direction_index + 1) % len(DIRECTIONS)
        self.heading = DIRECTIONS[new_direction_index]

    def turn_around(self):
        self.turn_right()
        self.turn_right()
