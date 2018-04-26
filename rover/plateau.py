from constraint import Constraint


class BoundaryConstraint(Constraint):
    """ This ensures that no movement is made outside of the plateau
    """
    def __init__(self, plateau=None):
        self.plateau = plateau

    def can_move(self, x=None, y=None, new_x=None, new_y=None, heading=None):
        size = self.plateau.size
        return all([
            new_x >= 0 and new_x <= size[0],
            new_y >= 0 and new_y <= size[1],
        ])


class Plateau(object):
    """ An encapsulation of the rectangular region on Mars
    """
    def __init__(self, size=(0, 0), constraint_classes=[]):
        self.size = size
        self.constraints = self.get_constraints(
            constraint_classes=constraint_classes)
        self.rovers = []

    def get_constraints(self, constraint_classes):
        constraints = []
        for constraint_class in constraint_classes:
            constraints.append(constraint_class(plateau=self))
        return constraints

    def add_rover(self, rover):
        rover.constraint = self
        self.rovers.append(rover)

    def is_move_valid(self, rover=None):
        """ Checks our constraints to determine whether the given rover
            can move
        """
        new_x, new_y = rover.coords_after_move
        x, y = rover.coords
        for constraint in self.constraints:
            if not constraint.can_move(
                    x=x, y=y,
                    new_x=new_x, new_y=new_y, heading=rover.heading):
                return False
        return True
