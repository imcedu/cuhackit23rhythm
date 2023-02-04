from math import sqrt

import Position

OFFSET = Position.GRID_PX * 11


class Note(object, Position):
    def __init__(self, direction, startpos, speed):
        self.direction = direction
        self.startpos = startpos
        self.position = startpos
        self.speed = speed if direction <= 3 else speed * sqrt(2)

    xDir = 0
    yDir = 0

    def spawn(self):
        pass

    def setMotion(self):

        match self.direction:
            case Position.Direction.C_UP:
                self.yDir = -1,
                pass
            case Position.Direction.C_DOWN:
                self.yDir = 1
                pass
            case Position.Direction.C_LEFT:
                self.xDir = -1
                pass
            case Position.Direction.C_RIGHT:
                self.xDir = 1
                pass
            case Position.Direction.D_UPLEFT:
                self.xDir = -1
                self.yDir = -1
                pass
            case Position.Direction.D_UPRIGHT:
                self.xDir = 1
                self.yDir = -1
                pass
            case Position.Direction.D_DNRIGHT:
                self.xDir = 1
                self.yDir = 1
                pass
            case Position.Direction.D_DNLEFT:
                self.xDir = -1
                self.yDir = 1
                pass

    def moveIn(self, xDir, yDir, speed):
        #while self.position != targetPositon:
        #    self.position.posX += xDir * speed
        #    self.position.posY += yDir * speed
            pass






