from math import sqrt
import Draw

CENTER_X = 385
CENTER_Y = 385
GRID_PX = 70
THRESHOLD = GRID_PX / 10
OFFSET = GRID_PX * 11
TARGET_C_UP_X = CENTER_X
TARGET_C_UP_Y = CENTER_Y - GRID_PX
TARGET_C_DOWN_X = CENTER_X
TARGET_C_DOWN_Y = CENTER_Y + GRID_PX
TARGET_C_LEFT_X = CENTER_X - GRID_PX
TARGET_C_LEFT_Y = CENTER_Y
TARGET_C_RIGHT_X = CENTER_X + GRID_PX
TARGET_C_RIGHT_Y = CENTER_Y
TARGET_D_UPLEFT_X = CENTER_X - GRID_PX
TARGET_D_UPLEFT_Y = CENTER_X - GRID_PX
TARGET_D_UPRIGHT_X = CENTER_X + GRID_PX
TARGET_D_UPRIGHT_Y = CENTER_Y - GRID_PX
TARGET_D_DNRIGHT_X = CENTER_X + GRID_PX
TARGET_D_DNRIGHT_Y = CENTER_Y + GRID_PX
TARGET_D_DNLEFT_X = CENTER_X - GRID_PX
TARGET_D_DNLEFT_Y = CENTER_Y + GRID_PX


class Note():
    def __init__(self, scr, direction, startXpos, startYpos, speed):
        self.direction = direction
        self.posX = startXpos
        self.posY = startYpos # Y-coordinate of tuple
        self.speed = speed if direction <= 3 else speed * sqrt(2)
        self.scr = scr
        self.xDir = 0
        self.yDir = 0
        self.targetposX = 0
        self.targetposY = 0
        self.destroyable = False
        self.setMotion()
        self.moveIn(scr, self.xDir, self.yDir, self.speed)

    def setMotion(self):

        match self.direction:
            # C_UP = 0,
            case 0:
                self.yDir = -1
                self.targetposX = TARGET_C_UP_X
                self.targetposY = TARGET_C_UP_Y
                pass

            # C_DOWN = 1,
            case 1:
                self.yDir = 1
                self.targetposX = TARGET_C_DOWN_X
                self.targetposY = TARGET_C_DOWN_Y
                pass

            # C_LEFT = 2,
            case 2:
                self.xDir = -1
                self.targetposX = TARGET_C_LEFT_X
                self.targetposY = TARGET_C_LEFT_Y
                pass
            
            # C_RIGHT = 3,
            case 3:
                self.xDir = 1
                self.targetposX = TARGET_C_RIGHT_X
                self.targetposY = TARGET_C_RIGHT_Y
                pass

            # D_UPLEFT = 4,
            case 4:
                self.xDir = -1
                self.yDir = -1
                self.targetposX = TARGET_D_UPLEFT_X
                self.targetposY = TARGET_D_UPLEFT_Y
                pass

            # D_UPRIGHT = 5,
            case 5:
                self.xDir = 1
                self.yDir = -1
                self.targetposX = TARGET_D_UPRIGHT_X
                self.targetposY = TARGET_D_UPRIGHT_Y
                pass

            # D_DNRIGHT = 6,
            case 6:
                self.xDir = 1
                self.yDir = 1
                self.targetposX = TARGET_D_DNRIGHT_X
                self.targetposY = TARGET_D_DNRIGHT_Y
                pass

            # D_DNLEFT = 7,
            case 7:
                self.xDir = -1
                self.yDir = 1
                self.targetposX = TARGET_D_DNLEFT_X
                self.targetposY = TARGET_D_DNLEFT_Y
                pass

    def moveIn(self, scr, xDir, yDir, speed):
        self.posX += xDir * speed
        self.posY += yDir * speed

        scr.erase(self)

        if abs(self.posX - self.targetposX) < THRESHOLD and abs(self.posY - self.targetposY) < THRESHOLD:
            self.destroyable = True
        else:
            scr.add(self)






