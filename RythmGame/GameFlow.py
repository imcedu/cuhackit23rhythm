import pygame as pg, os

WHITE = (255, 255, 255)
TITLE_SCREEN_IMAGE = pg.image.load(
    os.path.join('RythmGame/graphics','title_screen1_1.png'))
TITLE_SCREEN = pg.transform.scale(TITLE_SCREEN_IMAGE, (770,770))
START_TEXT = pg.image.load(
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
        pg.display.update()

    def does_collide(self, stick, note, WIN):
        if (abs(stick.posX - note.posX) <= 45 + THRESHOLD) and (abs(stick.posY - note.posY) <= 45 + THRESHOLD):
            return False
        if (abs(stick.posX - note.posX) <= 60 + THRESHOLD) and (abs(stick.posY - note.posY) <= 60 + THRESHOLD):
            return True

    def play_backtrack(self):
        pg.mixer.init()
        pg.mixer.music.load(file)
        pg.mixer.music.play()
        pg.event.wait()

