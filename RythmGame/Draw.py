import pygame, os, Note, JoyStick

GRID_SQUARE_SIZE = 70
GAMESCREEN_IMAGE = pygame.image.load(
    os.path.join('RythmGame/graphics', 'gamescreen.png'))
NOTE_C_UP = pygame.image.load(
    os.path.join('RythmGame/asteroids', 'north.png'))
NOTE_C_DOWN = pygame.image.load(
    os.path.join('RythmGame/asteroids', 'south.png'))
NOTE_C_LEFT = pygame.image.load(
    os.path.join('RythmGame/asteroids', 'west.png'))
NOTE_C_RIGHT = pygame.image.load(
    os.path.join('RythmGame/asteroids', 'east.png'))
NOTE_D_UPLEFT = pygame.image.load(
    os.path.join('RythmGame/asteroids', 'northwest.png'))
NOTE_D_UPRIGHT = pygame.image.load(
    os.path.join('RythmGame/asteroids', 'northeast.png'))
NOTE_D_DNRIGHT = pygame.image.load(
    os.path.join('RythmGame/asteroids', 'southeast.png'))
NOTE_D_DNLEFT = pygame.image.load(
    os.path.join('RythmGame/asteroids', 'southwest.png'))
QUIT_TEXT = pygame.image.load(os.path.join('RythmGame/graphics', 'quit_instructions.png'))
JOYSTICK_IMAGE = pygame.image.load(os.path.join('RythmGame/sprites', 'target.png'))
JOYSTICK = pygame.transform.scale(JOYSTICK_IMAGE, (150, 150))
JOYSTICK_OFFSET = 10

RED = (255, 0, 0)
BLUE = (0, 255, 0)

class Draw(object):
    def __init__(self):
        self.drawQueue = [] #list of objects that need to be drawn in the current frame

    def isOnScreen(self, obj):
        if obj in self.drawQueue:
            return True
        else:
            return False

    def add(self, obj):
        if not self.isOnScreen(obj):
            self.drawQueue.append(obj)
        pass

    #can be safely called for an object not yet on screen
    def erase(self, obj):
        if self.isOnScreen(obj): 
            self.drawQueue.remove(obj)
        pass

    def draw(self, WIN):

        self.draw_gamescreen(WIN)

        #loop through all of the objects in the queue and draw based on their type
        for o in self.drawQueue:
            if isinstance(o, Note.Note):
                match o.direction:
                    # C_UP = 0,
                    case 0:
                        image = NOTE_C_UP
                        pass

                    # C_DOWN = 1,
                    case 1:
                        image = NOTE_C_DOWN
                        pass

                    # C_LEFT = 2,
                    case 2:
                        image = NOTE_C_LEFT
                        pass
                    
                    # C_RIGHT = 3,
                    case 3:
                        image = NOTE_C_RIGHT
                        pass

                    # D_UPLEFT = 4,
                    case 4:
                        image = NOTE_D_UPLEFT

                    # D_UPRIGHT = 5,
                    case 5:
                        image = NOTE_D_UPRIGHT

                    # D_DNRIGHT = 6,
                    case 6:
                        image = NOTE_D_DNRIGHT

                    # D_DNLEFT = 7,
                    case 7:
                        image = NOTE_D_DNLEFT

                #image = pygame.transform.scale_by(image, 30)
                WIN.blit(image, (o.posX, o.posY))
            elif isinstance(o, JoyStick.JoyStick):
                #TODO: Replace placeholder shape with correct png
                WIN.blit(JOYSTICK, (o.posX - JOYSTICK_OFFSET, o.posY - JOYSTICK_OFFSET))
                pygame.display.update()

                #pygame.draw.rect(WIN, RED, pygame.Rect(o.posX, o.posY, GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))
        
        pygame.display.update()


    def draw_gamescreen(self, WIN):
        WIN.blit(GAMESCREEN_IMAGE, (0, 0))
        WIN.blit(QUIT_TEXT, (150,70))
        pygame.display.update()
