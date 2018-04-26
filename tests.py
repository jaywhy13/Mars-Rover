import unittest

from rover.constraint import Constraint
from rover.rover import Rover
from rover.constants import (
    HEADING_NORTH,
    HEADING_EAST,
    HEADING_SOUTH,
    HEADING_WEST,
    ACTION_LEFT,
    ACTION_RIGHT,
    ACTION_MOVE
)
from rover.plateau import Plateau, BoundaryConstraint
from rover.parser import Parser


class TestRover(unittest.TestCase):

    def test_default_kwargs(self):
        mars_rover = Rover()
        self.assertEqual(mars_rover.x, 0)
        self.assertEqual(mars_rover.y, 0)
        self.assertEqual(mars_rover.heading, HEADING_NORTH)
