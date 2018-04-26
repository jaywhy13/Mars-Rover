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

    def test_rotation(self):
        mars_rover = Rover()
        expected_headings = [
            HEADING_WEST, HEADING_SOUTH, HEADING_EAST, HEADING_NORTH]
        for i, expected_heading in enumerate(expected_headings):
            mars_rover.turn_left()
            self.assertEqual(mars_rover.heading, expected_headings[i])
        expected_headings = [
            HEADING_EAST, HEADING_SOUTH, HEADING_WEST, HEADING_NORTH]
        for i, expected_heading in enumerate(expected_headings):
            mars_rover.turn_right()
            self.assertEqual(mars_rover.heading, expected_headings[i])
        # we should be back at North
        self.assertEqual(mars_rover.heading, HEADING_NORTH)
        mars_rover.turn_left()
        mars_rover.turn_right()
        self.assertEqual(mars_rover.heading, HEADING_NORTH)
        mars_rover.turn_right()
        mars_rover.turn_left()
        self.assertEqual(mars_rover.heading, HEADING_NORTH)
        mars_rover.reset()
        mars_rover.turn_around()
        self.assertEqual(mars_rover.heading, HEADING_SOUTH)
        mars_rover.turn_right()
        mars_rover.turn_around()
        self.assertEqual(mars_rover.heading, HEADING_EAST)

    def test_movement(self):
        mars_rover = Rover()
        # test moving up
        mars_rover.move()
        self.assertEqual(mars_rover.coords, (0, 1))
        mars_rover.reset()
        # test moving down
        mars_rover.turn_around()
        mars_rover.move()
        self.assertEqual(mars_rover.coords, (0, -1))
        mars_rover.reset()
        # test left movement
        mars_rover.turn_left()
        mars_rover.move()
        self.assertEqual(mars_rover.coords, (-1, 0))
        mars_rover.reset()
        # test right movement
        mars_rover.turn_right()
        mars_rover.move()
        self.assertEqual(mars_rover.coords, (1, 0))
        mars_rover.reset()


class TestPlateau(unittest.TestCase):

    def test_init(self):
        plateau = Plateau(size=(5, 5))
        self.assertEqual(plateau.size, (5, 5))
        mars_rover = Rover(plateau=plateau)
        self.assertEqual(mars_rover.plateau, plateau)

    def test_boundary_constraints(self):
        plateau = Plateau(
            size=(1, 1),
            constraint_classes=[BoundaryConstraint])
        mars_rover = Rover(plateau=plateau)
        self.assertTrue(mars_rover.can_move())
        mars_rover.move()
        self.assertFalse(mars_rover.can_move())
        mars_rover.reset()
        self.assertTrue(mars_rover.can_move())
        mars_rover.turn_left()
        mars_rover.move()
        self.assertFalse(mars_rover.can_move())
        mars_rover.reset()
        mars_rover.turn_around()
        self.assertFalse(mars_rover.can_move())


class TestParser(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_parse_plateau_params(self):
        parsed_params = self.parser.parse_plateau_params("Plateau:5 5")
        self.assertEqual(
            parsed_params.get("size"), (5, 5))

    def test_parse_rover_params(self):
        parsed_params = self.parser.parse_rover_params(
            "Rover1 Landing:1 2 N")
        self.assertEqual(parsed_params.get("x"), 1)
        self.assertEqual(parsed_params.get("y"), 2)
        self.assertEqual(parsed_params.get("heading"), "N")

    def test_parse_rover_instructions(self):
        instructions = list("LMLMLMLMM")
        parsed_instructions = self.parser.parse_rover_instructions(
            "Rover1 Instructions:{}".format("".join(instructions)))
        self.assertEqual(parsed_instructions, instructions)

    def test_parse_rover_instruction(self):
        mars_rover = Rover()
        self.parser.process_rover_instruction(
            rover=mars_rover, instruction=ACTION_LEFT)
        self.assertEqual(mars_rover.heading, HEADING_WEST)
        mars_rover.reset()
        self.parser.process_rover_instruction(
            rover=mars_rover, instruction=ACTION_RIGHT)
        self.assertEqual(mars_rover.heading, HEADING_EAST)
        mars_rover.reset()
        self.parser.process_rover_instruction(
            rover=mars_rover, instruction=ACTION_MOVE)
        self.assertEqual(mars_rover.coords.y, 1)


