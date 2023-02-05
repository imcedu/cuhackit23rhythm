from math import sqrt
import Draw


GRID_PX = 70
THRESHOLD = GRID_PX / 10
OFFSET = GRID_PX * 11


class Note():
    def __init__(self, scr, direction, startXpos, startYpos, speed):
        self.direction = direction
        self.posX = startXpos
        self.posY = startYpos # Y-coordinate of tuple
        self.speed = speed if direction <= 3 else speed * sqrt(2)
        self.scr = scr
        self.xDir = 0
        self.yDir = 0
        self.setMotion()
        self.moveIn(scr, self.xDir, self.yDir, self.speed)

    def setMotion(self):

        match self.direction:
            # C_UP = 0,
            case 0:
                self.yDir = -1
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

    def moveIn(self, scr, xDir, yDir, speed):
        self.posX += xDir * speed
        self.posY += yDir * speed
        scr.erase(self)
        scr.add(self)






