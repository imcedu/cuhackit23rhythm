import pygame, os

WHITE = (255, 255, 255)
TITLE_SCREEN_IMAGE = pygame.image.load(
    os.path.join('RythmGame/graphics','title_screen1_1.png'))
TITLE_SCREEN = pygame.transform.scale(TITLE_SCREEN_IMAGE, (770,770))
START_TEXT = pygame.image.load(
    os.path.join('RythmGame/graphics', 'start_instructions.png'))

THRESHOLD = 10

class GameFlow():
    def __init__(self):
        pass

    def draw_title(self, WIN):
        WIN.fill(WHITE)
        WIN.blit(TITLE_SCREEN, (0, 0))
        WIN.blit(START_TEXT, (0,0))
        pygame.display.update()

    def does_collide(stick, note, WIN):
        if abs(stick.posX + 35 - note.posX) <= 35 + THRESHOLD and abs(stick.posX + 35 - note.posX) <= 35 + THRESHOLD:
            return True

        

    def play_backtrack(self):
        pass

    def play_note(self):
        pass
