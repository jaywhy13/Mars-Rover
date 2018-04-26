from rover.rover import Rover
from rover.plateau import Plateau
from rover.constants import (
    ACTION_LEFT,
    ACTION_RIGHT,
    ACTION_MOVE
)


class Parser(object):

    def process_input(self):
        plateau = Plateau(**self.parse_plateau_params(line=input()))
        positions = []
        for i in range(2):
            name = "Rover{}".format(i + 1)
            rover = Rover(**self.parse_rover_params(line=input()))
            instructions = self.parse_rover_instructions(line=input())
            self.process_rover_instructions(
                rover=rover, instructions=instructions)
            positions.append(self.get_rover_position(name=name, rover=rover))
        for position in positions:
            print(position)

    def parse_plateau_params(self, line=None):
        """ Gets parameters to intiialize the Plateau
        """
        size_string = line.split(":")[1]
        size = tuple(map(int, size_string.split(" ")))
        return dict(size=size)

    def parse_rover_params(self, line=None):
        """ Gets parameters to initialize the Rover
        """
        coords_and_heading = line.split(":")[1]
        x, y, heading = coords_and_heading.split(" ")
        return dict(x=int(x), y=int(y), heading=heading)

    def parse_rover_instructions(self, line=None):
        """ Pulls out the instructions from the command line
        """
        return list(line.split(":")[1])

    def process_rover_instructions(self, rover, instructions):
        for instruction in instructions:
            self.process_rover_instruction(rover, instruction)

    def process_rover_instruction(self, rover, instruction):
        if instruction == ACTION_MOVE:
            rover.move()
        elif instruction == ACTION_LEFT:
            rover.turn_left()
        elif instruction == ACTION_RIGHT:
            rover.turn_right()

    def get_rover_position(self, name=None, rover=None):
        """ Returns the rover position in the expected format
        """
        return "{}:{} {} {}".format(
            name, rover.x, rover.y, rover.heading)
