GRID_PX = 70
THRESHOLD = GRID_PX / 10


class Position(object):
    def __init__(self):
        self.posX
        self.posY

    def __eq__(self, other):
        if self.posX >= other.posX - THRESHOLD and self.posX <= other.posX + THRESHOLD and self.posY >= other.posY - THRESHOLD and self.posY <= other.posY + THRESHOLD:
            return True
        else:
            return False


