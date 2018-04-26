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

