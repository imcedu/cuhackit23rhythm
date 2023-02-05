
import pygame, Draw


RED = (255, 0, 0)
GRID_SQUARE_SIZE = 70

class JoyStick():  
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color
        self.isStrummed = False

    def move_stick(self, WIN, keys_pressed):
        if keys_pressed[pygame.K_a]: #LEFT
            self.posX = self.posX - GRID_SQUARE_SIZE

        if keys_pressed[pygame.K_d]: #RIGHT
            self.posX = self.posX + GRID_SQUARE_SIZE
        
        if keys_pressed[pygame.K_w]: #UP
            self.posY = self.posY - GRID_SQUARE_SIZE

        if keys_pressed[pygame.K_s]: #DOWN
            self.posY = self.posY + GRID_SQUARE_SIZE

        # Draw the joystick in the new location
        Draw.Draw.add(self)

    def reset_stick(self, start_index):
        self.posX = start_index
        self.posY = start_index
        self.isStrummed = False
        Draw.Draw.erase(self)
        
    # Strum is set to true when SPACE is pressed
    def strum(self):
        self.isStrummed = True


