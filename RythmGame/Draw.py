import pygame

GRID_SQUARE_SIZE = 70
RED = (255, 0, 0)
BLUE = (0, 255, 0)

class Draw(object):
    def __init__(self):
        self.drawQueue = []
        pass

    def isOnScreen(self, obj):
        if self.drawQueue.find(obj):
            return True
        else:
            return False

    def add(self, obj):
        if not self.isOnScreen(self, obj):
            self.drawQueue.append(obj)
        pass

    def erase(self, obj):
        if self.isOnScreen(self, obj):
            self.drawQueue.remove(obj)
        pass

    def draw(self, WIN):
        for o in self.drawQueue:
            if hasattr(o, '__Note__'):
                pygame.draw.rect(WIN, BLUE, pygame.Rect(o.position.posX, o.position.posY, GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))
            elif hasattr(o, '__JoyStick__'):
                pygame.draw.rect(WIN, RED, pygame.Rect(o.posX, o.posY, GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))
        pass