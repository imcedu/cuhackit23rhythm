import pygame, os

WHITE = (255, 255, 255)
TITLE_SCREEN_IMAGE = pygame.image.load(
    os.path.join('RythmGame/graphics','title_screen1_1.png'))
TITLE_SCREEN = pygame.transform.scale(TITLE_SCREEN_IMAGE, (770,770))
START_TEXT = pygame.image.load(
    os.path.join('RythmGame/graphics', 'start_instructions.png'))

THRESHOLD = 0
file = 'RythmGame/music/astro_beats_2.mp3'

class GameFlow():
    def __init__(self):
        pass

    def draw_title(self, WIN):
        WIN.fill(WHITE)
        WIN.blit(TITLE_SCREEN, (0, 0))
        WIN.blit(START_TEXT, (0,0))
        pygame.display.update()

    def does_collide(self, stick, note, WIN):
        if (abs(stick.posX - note.posX) <= 35 + THRESHOLD) and (abs(stick.posY - note.posY) <= 35 + THRESHOLD):
            return False
        if (abs(stick.posX - note.posX) <= 45 + THRESHOLD) and (abs(stick.posY - note.posY) <= 45 + THRESHOLD):
            return True

    def play_backtrack(self):
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        pygame.event.wait()

