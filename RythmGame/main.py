import pygame, os, GameFlow, Draw, Note, NoteMapper

WIDTH, HEIGHT = 770, 770
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Astro Beats")



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 60
RESTING_JOYSTICK_POSITION = 350
NOTE_LOOKAHEAD_OFFSET = 180


def main():
    clock = pygame.time.Clock()
    game_flow = GameFlow.GameFlow()
    game_flow.draw_title(WIN)
    screen = Draw.Draw()
    run = True
    started = False
    mapper = NoteMapper.NoteMapper()
    map = mapper.map
    currNotes = []

    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    screen.draw(WIN)
                    started = True
                    frameCounter = -1 #incremented at end of every tick, so will start at 0
                    #TODO: play the song here
                if event.key == pygame.K_ESCAPE:
                    run = False
        if started:
            frameCounter += 1
            if int(map[0][1]) - frameCounter <= NOTE_LOOKAHEAD_OFFSET:
                 startXpos, startYpos  = getStartPos(map[0][0])
                 note = Note.Note(screen, map[0][0], startXpos, startYpos, NOTE_LOOKAHEAD_OFFSET / FPS)
                 currNotes.append(note)
                 map.pop(0)
            for n in currNotes:
                n.moveIn(screen, n.xDir, n.yDir, n.speed)
            screen.draw(WIN)


    pygame.quit()

def getStartPos(direction):
    match direction:
        # C_UP = 0,
        case 0:
            result = ((WIDTH * 0.5), (HEIGHT + HEIGHT * 0.5))
            return result

        # C_DOWN = 1,
        case 1:
            result = ((WIDTH * 0.5), (0 - HEIGHT * 0.5))
            return result

        # C_LEFT = 2,
        case 2:
            result = ((WIDTH + WIDTH * 0.5), (HEIGHT * 0.5))
            return result
            
        # C_RIGHT = 3,
        case 3:
            result = ((0 - WIDTH * 0.5), (HEIGHT * 0.5))
            return result

        # D_UPLEFT = 4,
        case 4:
            result = ((WIDTH + WIDTH * 0.5), (HEIGHT + HEIGHT * 0.5))
            return result

        # D_UPRIGHT = 5,
        case 5:
            result = ((0 - WIDTH * 0.5), (HEIGHT + HEIGHT * 0.5))
            return result

        # D_DNRIGHT = 6,
        case 6:
            result = ((0 - WIDTH * 0.5), (0 - HEIGHT * 0.5))
            return result

        # D_DNLEFT = 7,
        case 7:
            result = ((WIDTH + WIDTH * 0.5), (0 - HEIGHT * 0.5))
            return result   

if __name__ == "__main__":
    main()