
import pygame as pg, Draw


RED = (255, 0, 0)
GRID_SQUARE_SIZE = 70
RESTING_JOYSTICK_POSITION = 350

class JoyStick():  
    def __init__(self, posX, posY, color):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.isStrummed = False

    def move_stick(self, WIN, keys_pressed, screen):
        # No direction is inputed, therefore reset stick to center
        if (keys_pressed[pygame.K_a] == 0 and keys_pressed[pygame.K_d] == 0 and keys_pressed[pygame.K_w] == 0 and keys_pressed[pygame.K_s] == 0):
            self.reset_stick(RESTING_JOYSTICK_POSITION, screen)

        if keys_pressed[pygame.K_a]: #LEFT
            if(self.posX > RESTING_JOYSTICK_POSITION - GRID_SQUARE_SIZE):
                self.posX = self.posX - GRID_SQUARE_SIZE

        if keys_pressed[pygame.K_d]: #RIGHT
            if(self.posX < RESTING_JOYSTICK_POSITION + GRID_SQUARE_SIZE):
                self.posX = self.posX + GRID_SQUARE_SIZE
        
        if keys_pressed[pygame.K_w]: #UP
            if(self.posY > RESTING_JOYSTICK_POSITION - GRID_SQUARE_SIZE):
                self.posY = self.posY - GRID_SQUARE_SIZE

        if keys_pressed[pygame.K_s]: #DOWN
            if(self.posY < RESTING_JOYSTICK_POSITION + GRID_SQUARE_SIZE):
                self.posY = self.posY + GRID_SQUARE_SIZE

        # Draw the joystick in the new location
        screen.add(self)

    def reset_stick(self, start_index, screen):
        self.posX = start_index
        self.posY = start_index
        self.isStrummed = False
        screen.erase(self)
        
    # Strum is set to true when SPACE is pressed
    def strum(self):
        self.isStrummed = True


