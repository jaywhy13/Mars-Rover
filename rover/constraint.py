class Constraint(object):
    """ This class encapsulates constraints on the movement.
        It simply tells us if it possible to move.
    """
    def can_move(self, x=None, y=None, new_x=None, new_y=None, heading=None):
        """ Returns True if it's possible to move given the current
            heading, and x and y pos and new x and y
        """
        return True
