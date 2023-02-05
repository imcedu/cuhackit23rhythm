import pygame, os

GRID_SQUARE_SIZE = 70
GAMESCREEN_IMAGE = pygame.image.load(
    os.path.join('RythmGame/graphics', 'gamescreen.png'))
QUIT_TEXT = pygame.image.load(os.path.join('RythmGame/graphics', 'quit_instructions.png'))

RED = (255, 0, 0)
BLUE = (0, 255, 0)

class Draw(object):
    def __init__(self):
        self.drawQueue = [] #list of objects that need to be drawn in the current frame

    def isOnScreen(self, obj):
        if self.drawQueue.find(obj):
            return True
        else:
            return False

    def add(self, obj):
        if not self.isOnScreen(self, obj):
            self.drawQueue.append(obj)
        pass

    #can be safely called for an object not yet on screen
    def erase(self, obj):
        if self.isOnScreen(self, obj): 
            self.drawQueue.remove(obj)
        pass

    def draw(self, WIN):

        self.draw_gamescreen(WIN)

        #loop through all of the objects in the queue and draw based on their type
        for o in self.drawQueue:
            if hasattr(o, '__Note__'):
                #TODO: Replace placeholder shape with correct pngs (will make use of both position and direction)
                pygame.draw.rect(WIN, BLUE, pygame.Rect(o.position.posX, o.position.posY, GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))
            elif hasattr(o, '__JoyStick__'):
                #TODO: Replace placeholder shape with correct png
                pygame.draw.rect(WIN, RED, pygame.Rect(o.posX, o.posY, GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))
        
        pygame.display.update()

        pass

    def draw_gamescreen(self, WIN):
        WIN.blit(GAMESCREEN_IMAGE, (0, 0))
        WIN.blit(QUIT_TEXT, (150,70))
        pygame.display.update()