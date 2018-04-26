import re

from rover import Rover
from plateau import Plateau
from constants import (
    ACTION_LEFT,
    ACTION_RIGHT,
    ACTION_MOVE
)

try:
   input = raw_input
except NameError:
   pass


class Parser(object):

    PLATEAU_INPUT = r'Plateau:(?P<x>[0-9]+) (?P<y>[0-9]+)'
    PLATEAU_INPUT_DESCRIPTION = 'Plateau:<x> <y>'

    ROVER_LANDING_INPUT = \
        r'(?P<rover_name>Rover[0-9]+) Landing:(?P<x>[0-9]+) (?P<y>[0-9]+) (?P<heading>[NSEW])'
    ROVER_LANDING_INPUT_DESCRIPTION = 'Rover<number> Landing:<x> <y>'

    ROVER_INSTRUCTIONS_INPUT = \
        r'(?P<rover_name>Rover[0-9]+) Instructions:(?P<instructions>[MRL]+)'
    ROVER_INSTRUCTIONS_INPUT_DESCRIPTION = \
        'Rover<number> Instructions:<instructions>'

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

    def parse_input_with_regex(
            self, text=None, regex=None, regex_description=None):
        """ Parses the input with the given regex. Raises a ValueError
            based on the description if the format is not met. Returns
            a dictionary
        """
        match = re.match(regex, (text or "").strip())
        if not match:
            raise ValueError(
                "Input '{}' did not match the given format: {}".format(
                    text, regex_description))
        return match.groupdict()

    def parse_plateau_params(self, line=None):
        """ Gets parameters to intiialize the Plateau
        """
        params = self.parse_input_with_regex(
            text=line,
            regex=Parser.PLATEAU_INPUT,
            regex_description=Parser.PLATEAU_INPUT_DESCRIPTION)
        x = int(params.get("x"))
        y = int(params.get("y"))
        return dict(size=(x, y))

    def parse_rover_params(self, line=None):
        """ Gets parameters to initialize the Rover
        """
        params = self.parse_input_with_regex(
            text=line,
            regex=Parser.ROVER_LANDING_INPUT,
            regex_description=Parser.ROVER_LANDING_INPUT_DESCRIPTION)
        x = int(params.get("x"))
        y = int(params.get("y"))
        heading = params.get("heading")
        return dict(x=x, y=y, heading=heading)

    def parse_rover_instructions(self, line=None):
        """ Pulls out the instructions from the command line
        """
        params = self.parse_input_with_regex(
            text=line,
            regex=Parser.ROVER_INSTRUCTIONS_INPUT,
            regex_description=Parser.ROVER_INSTRUCTIONS_INPUT_DESCRIPTION)
        instructions = list(params.get("instructions"))
        return instructions

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
