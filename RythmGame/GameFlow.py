import pygame, os

WHITE = (255, 255, 255)

TITLE_SCREEN_IMAGE = pygame.image.load(
    os.path.join('RythmGame/graphics','title_screen1_1.png'))
TITLE_SCREEN = pygame.transform.scale(TITLE_SCREEN_IMAGE, (770,770))
START_TEXT = pygame.image.load(
    os.path.join('RythmGame/graphics', 'start_instructions.png'))
GAMESCREEN_IMAGE = pygame.image.load(
    os.path.join('RythmGame/graphics', 'gamescreen.png'))
QUIT_TEXT = pygame.image.load(os.path.join('RythmGame/graphics', 'quit_instructions.png'))

class GameFlow():
    def __init__(self):
        pass

    def draw_title(self, WIN):
        WIN.fill(WHITE)
        WIN.blit(TITLE_SCREEN, (0, 0))
        WIN.blit(START_TEXT, (0,0))
        pygame.display.update()

    def draw_gamescreen(self, WIN):
        WIN.blit(GAMESCREEN_IMAGE, (0, 0))
        WIN.blit(QUIT_TEXT, (150,70))
        pygame.display.update()

    def handle_collisions(self):
        pass

    def play_backtrack(self):
        pass

    def play_note(self):
        pass
