from math import sqrt
import Draw


GRID_PX = 70
THRESHOLD = GRID_PX / 10
OFFSET = GRID_PX * 11


class Note():
    def __init__(self, direction, startpos, speed):
        self.direction = direction
        self.pos = startpos
        self.speed = speed if direction <= 3 else speed * sqrt(2)
        self.moveIn()

    xDir = 0
    yDir = 0

    def setMotion(self):

        match self.direction:
            # C_UP = 0,
            case 0:
                self.yDir = -1,
                pass

            # C_DOWN = 1,
            case 1:
                self.yDir = 1
                pass

            # C_LEFT = 2,
            case 2:
                self.xDir = -1
                pass
            
            # C_RIGHT = 3,
            case 3:
                self.xDir = 1
                pass

            # D_UPLEFT = 4,
            case 4:
                self.xDir = -1
                self.yDir = -1
                pass

            # D_UPRIGHT = 5,
            case 5:
                self.xDir = 1
                self.yDir = -1
                pass

            # D_DNRIGHT = 6,
            case 6:
                self.xDir = 1
                self.yDir = 1
                pass

            # D_DNLEFT = 7,
            case 7:
                self.xDir = -1
                self.yDir = 1
                pass

    def moveIn(self, xDir, yDir, speed):
        #while self.pos != targetPositon:
            self.pos.first += xDir * speed
            self.pos.second += yDir * speed
            Draw.remove(self)
            Draw.add(self)






