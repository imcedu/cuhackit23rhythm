import pygame as pg, os, Note, JoyStick

GRID_SQUARE_SIZE = 70
GAMESCREEN_IMAGE = pg.image.load(
    os.path.join('RythmGame/graphics', 'gamescreen.png'))
NOTE_C_UP = pg.image.load(
    os.path.join('RythmGame/asteroids', 'north.png'))
NOTE_C_DOWN = pg.image.load(
    os.path.join('RythmGame/asteroids', 'south.png'))
NOTE_C_LEFT = pg.image.load(
    os.path.join('RythmGame/asteroids', 'west.png'))
NOTE_C_RIGHT = pg.image.load(
    os.path.join('RythmGame/asteroids', 'east.png'))
NOTE_D_UPLEFT = pg.image.load(
    os.path.join('RythmGame/asteroids', 'northwest.png'))
NOTE_D_UPRIGHT = pg.image.load(
    os.path.join('RythmGame/asteroids', 'northeast.png'))
NOTE_D_DNRIGHT = pg.image.load(
    os.path.join('RythmGame/asteroids', 'southeast.png'))
NOTE_D_DNLEFT = pg.image.load(
    os.path.join('RythmGame/asteroids', 'southwest.png'))

ASTEROID = pg.image.load(
    os.path.join('RythmGame/asteroids', 'smaller_asteroid.png'))
    
QUIT_TEXT = pg.image.load(os.path.join('RythmGame/graphics', 'quit_instructions.png'))
JOYSTICK = pg.image.load(os.path.join('RythmGame/sprites', 'RESIZED_.png'))
JOYSTICK_OFFSET = 35
ASTEROID_OFFSET = 15

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

    def explosion(self, obj, WIN):
        pg.draw.rect(WIN, RED, pg.Rect(obj.posX, obj.posY, 25, 25))
        pg.display.update()

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
                        image = ASTEROID

                    # C_DOWN = 1,
                    case 1:
                        image = ASTEROID

                    # C_LEFT = 2,
                    case 2:
                        image = ASTEROID
                    
                    # C_RIGHT = 3,
                    case 3:
                        image = ASTEROID

                    # D_UPLEFT = 4,
                    case 4:
                        image = ASTEROID

                    # D_UPRIGHT = 5,
                    case 5:
                        image = ASTEROID

                    # D_DNRIGHT = 6,
                    case 6:
                        image = ASTEROID

                    # D_DNLEFT = 7,
                    case 7:
                        image = ASTEROID

                #image = pg.transform.scale_by(image, 30)
                WIN.blit(image, (o.posX - ASTEROID_OFFSET, o.posY - ASTEROID_OFFSET))
            elif isinstance(o, JoyStick.JoyStick):
                WIN.blit(JOYSTICK, (o.posX - JOYSTICK_OFFSET, o.posY - JOYSTICK_OFFSET))
        
        pg.display.flip()


    def draw_gamescreen(self, WIN):
        WIN.blit(GAMESCREEN_IMAGE, (0, 0))
        WIN.blit(QUIT_TEXT, (150,70))
