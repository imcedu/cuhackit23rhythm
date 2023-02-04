from enum import Enum

GRID_PX = 70
THRESHOLD = GRID_PX / 10


class Direction(Enum):
    C_UP = 0,
    C_DOWN = 1,
    C_LEFT = 2,
    C_RIGHT = 3,
    D_UPLEFT = 4,
    D_UPRIGHT = 5,
    D_DNRIGHT = 6,
    D_DNLEFT = 7


class Position(object):
    def __init__(self):
        self.posX
        self.posY

    def __eq__(self, other):
        if self.posX >= other.posX - THRESHOLD and self.posX <= other.posX + THRESHOLD and self.posY >= other.posY - THRESHOLD and self.posY <= other.posY + THRESHOLD:
            return True
        else:
            return False


